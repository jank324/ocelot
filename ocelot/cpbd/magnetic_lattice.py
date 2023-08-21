import logging
import re
from collections import defaultdict
from typing import Any, Callable, Generator, Iterator, Mapping, Sequence, Tuple

import numpy as np

from ocelot.cpbd.elements.bend import Bend
from ocelot.cpbd.elements.drift import Drift
from ocelot.cpbd.elements.element import Element
from ocelot.cpbd.elements.marker import Marker
from ocelot.cpbd.elements.matrix import Matrix
from ocelot.cpbd.elements.monitor import Monitor
from ocelot.cpbd.elements.rbend import RBend
from ocelot.cpbd.elements.sbend import SBend
from ocelot.cpbd.elements.undulator import Undulator
from ocelot.cpbd.elements.unknown_element import UnknownElement
from ocelot.cpbd.latticeIO import LatticeIO
from ocelot.cpbd.optics import lattice_transfer_map
from ocelot.cpbd.tm_utils import transfer_maps_mult
from ocelot.cpbd.transformations.transfer_map import TransferMap

_logger = logging.getLogger(__name__)

# Returned by insert_marker_by_type, insert_markers_by_name,
# insert_markers_by_predicate
MarkersInsertionReturnType = Mapping[Element, Sequence[Tuple[Marker, Marker]]]


def lattice_format_converter(elements):
    """
    :param elements: lattice in the format: [[elem1, center_pos1], [elem2, center_pos2], [elem3, center_pos3], ... ]
    :return: lattice in the format: [elem1, drift1, elem2, drift2, elem3, drift3, ...]
    """
    cell = []
    drift_num = 0
    s_pos = 0.0
    for element in elements:
        element_start = element[1] - element[0].l / 2.0
        if (
            element_start < s_pos - 1.0e-14
        ):  # 1.0e-14 is used as crutch for precision of float
            if element[0].l == 0.0:
                if s_pos - element_start > 1.0e-2:
                    print(
                        "************** WARNING! Element "
                        + element[0].id
                        + " was deleted"
                    )
                    continue
                element[1] = s_pos
                print(
                    "************** WARNING! Element "
                    + element[0].id
                    + " was moved from "
                    + str(element_start)
                    + " to "
                    + str(s_pos)
                )
            else:
                dl = element[0].l / 2.0 - element[1] + s_pos
                if (
                    cell[-1].__class__ == Marker
                    and cell[-2].__class__ == Drift
                    and cell[-2].l > dl
                ):
                    cell[-2].l -= dl
                    print(
                        "************** WARNING! Element "
                        + cell[-1].id
                        + " was deleted"
                    )
                    cell.pop()
                else:
                    print(
                        "************** ERROR! Element "
                        + element[0].id
                        + " has bad position (overlapping?)"
                    )
                    exit()

        if (
            element_start > s_pos + 1.0e-12
        ):  # 1.0e-12 is used as crutch for precision of float
            drift_num += 1
            drift_l = round(
                element_start - s_pos, 10
            )  # round() is used as crutch for precision of float
            drift_eid = "D_" + str(drift_num)
            cell.append(Drift(l=drift_l, eid=drift_eid))

        cell.append(element[0])
        s_pos = element[1] + element[0].l / 2.0
    return tuple(cell)


def merger(lat, remaining_types=None, remaining_elems=None, init_energy=0.0):
    """
    Function to compress the lattice excluding elements by type or by individual elements

    :param lat: MagneticLattice
    :param remaining_types: list, the type of the elements which needed to be untouched
                            others will be "compress" to Matrix element
                            e.g. [Monitor, Quadrupole, Bend, Hcor]
    :param remaining_elems: list of elements (ids (str) or object)
    :param init_energy: initial energy
    :return: New MagneticLattice
    """
    if remaining_elems is None:
        remaining_elems = []
    if remaining_types is None:
        remaining_types = []
    _logger.debug("element numbers before: " + str(len(lat.sequence)))
    lattice_analysis = []
    merged_elems = []
    for elem in lat.sequence:
        if (
            elem.__class__ in remaining_types
            or elem.id in remaining_elems
            or elem in remaining_elems
        ):
            lattice_analysis.append(merged_elems)
            merged_elems = []
            lattice_analysis.append([elem])
        else:
            merged_elems.append(elem)
    if len(merged_elems) != 0:
        lattice_analysis.append(merged_elems)

    seq = []
    E = init_energy
    for elem_list in lattice_analysis:
        if len(elem_list) == 1:
            for tm in elem_list[0].tms:
                E += tm.get_delta_e()
            seq.append(elem_list[0])
        elif len(elem_list) == 0:
            continue
        else:
            magnetic_elems = [
                elem
                for elem in elem_list
                if elem.__class__ not in [Marker, Drift, Monitor]
            ]
            if len(magnetic_elems) == 0:
                total_len = np.sum([elem.l for elem in elem_list])
                d = Drift(l=total_len)
                seq.append(d)
            else:
                delta_e = np.sum(
                    [tm.get_delta_e() for elem in elem_list for tm in elem.tms]
                )
                lattice = MagneticLattice(elem_list, method=lat.method)
                m = Matrix()
                m.b, m.r, m.t = lattice.transfer_maps(energy=E)
                m.l = lattice.totalLen
                m.delta_e = delta_e
                E += delta_e
                seq.append(m)

    new_lat = MagneticLattice(seq, method=lat.method)
    _logger.debug("element numbers after: " + str(len(new_lat.sequence)))
    return new_lat


def flatten(iterable: Iterator[Any]) -> Generator[Any, None, None]:
    """Flatten arbitrarily nested iterable.
    Special case for strings that avoids infinite recursion.  Non iterables passed
    as arguments are yielded.

    :param iterable: Any iterable to be flattened.
    :raises: RecursionError

    """

    def _flatten(iterable):
        try:
            for item in iterable:
                try:
                    iter(item)
                except TypeError:
                    yield item
                else:
                    yield from _flatten(item)
        except TypeError:  # If iterable isn't actually iterable, then yield it.
            yield iterable

    try:
        yield from _flatten(iterable)
    except RecursionError:
        raise RecursionError(
            "Maximum recusion reached.  Possibly trying"
            " to flatten an infinitely nested iterable."
        )


class MagneticLattice:
    """
    sequence - list of the elements,
    start - first element of lattice. If None, then lattice starts from first element of sequence,
    stop - last element of lattice. If None, then lattice stops by last element of sequence,
    method - A dictionary that contains the method of the tracking. If nothing is set TransferMap will
    be used as the global method for all elements. Setting TransferMaps for specific elements is also possible.
    Notes: If the elements doesn't support the defined transfer map, the default transfer map will be used, which is
    defined in the specific element class.
    For example:
        {"global": SecondTM, "Undulator": UndulatorTestTM }
        Sets for all elements SecondTM as transfer map, expect for the Undulator elements.
    """

    def __init__(self, sequence, start=None, stop=None, method=None):
        if method is None:
            method = {"global": TransferMap}
        if isinstance(method, dict):
            self.method = method
        else:
            self.method = method.to_dict()

        self.sequence = list(flatten(sequence))
        self.sequence = self.get_sequence_part(start, stop)

        # create transfer map and calculate lattice length
        self.totalLen = 0

        self.update_transfer_maps()

        self.__hash__ = {}
        for e in self.sequence:
            self.__hash__[e] = e

    def get_sequence_part(self, start, stop):
        try:
            if start is not None:
                id1 = self.sequence.index(start)
            else:
                id1 = 0
            if stop is not None:
                id2 = self.sequence.index(stop) + 1
                sequence = self.sequence[id1:id2]
            else:
                sequence = self.sequence[id1:]
        except:
            print("cannot construct sequence, element not found")
            raise
        return sequence

    def __getitem__(self, el):
        try:
            return self.__hash__[el]
        except:
            return None

    def update_transfer_maps(self):
        self.totalLen = 0
        for i, element in enumerate(self.sequence):
            # TODO: This belongs to the Element Undulator
            if element.__class__ == Undulator:
                if element.field_file is not None:
                    element.l = element.field_map.l * element.field_map.field_file_rep
                    if element.field_map.units == "mm":
                        element.l = element.l * 0.001
            self.totalLen += element.l

            tm_class_type = self.method.get(element.__class__)
            if tm_class_type:
                element.set_tm(tm_class_type)
            else:
                tm_class_type = self.method.get("global")
                if tm_class_type:
                    element.set_tm(tm_class_type)

            _logger.debug(
                f"update: {','.join([tm.__class__.__name__ for tm in element.tms])}"
            )
        return self

    def update_endings(self, lat_index, element, body_elements, element_util):
        if element_util.suffix_1 in element.id:
            body = self.sequence[lat_index + 1]
            if body.__class__ not in body_elements:
                body = self.sequence[lat_index - 1]
                _logger.debug("Backtracking?")
            element_util.update_first(element, body)
        elif element_util.suffix_2 in element.id:
            body = self.sequence[lat_index - 1]
            if body.__class__ not in body_elements:
                body = self.sequence[lat_index + 1]
                _logger.debug("Backtracking?")
            element_util.update_last(element, body)
        else:
            _logger.error(
                element.__class__.__name__
                + " is not updated. Use standard function to create and update MagneticLattice"
            )

    def __str__(self):
        line = "LATTICE: length = " + str(self.totalLen) + " m \n"
        for e in self.sequence:
            line += "{0:15} length: {1:5.2f}      id: {2:10}\n".format(
                e.__class__.__name__, e.l, e.id
            )
        return line

    def find_indices(self, element):
        indx_elem = np.where([i.__class__ == element for i in self.sequence])[0]
        return indx_elem

    def find_drifts(self):
        drift_lengs = []
        drifts = []
        for elem in self.sequence:
            if elem.__class__ == Drift:
                elem_l = np.around(elem.l, decimals=6)
                if elem_l not in drift_lengs:
                    drifts.append(elem)
                    drift_lengs.append(elem_l)
        return drifts

    def rem_drifts(self):
        drifts = {}
        for i, elem in enumerate(self.sequence):
            if elem.__class__ == Drift:
                if not (elem.l in drifts.keys()):
                    drifts[elem.l] = elem
                else:
                    self.sequence[i] = drifts[elem.l]

    def save_as_py_file(
        self, file_name: str, tws0=None, remove_rep_drifts=True, power_supply=False
    ):
        """
        Saves the lattice in a python file.
        :param file_name: path and python file name where the lattice will be stored
        :param tws0: None or Twiss object. If Twiss object then twiss parameters will be printed in the beginning of
                    lattice file
        :param remove_rep_drifts: removes the drift elements
        :param power_supply: Writes the power supply ids in the file
        :return: None
        """
        LatticeIO.save_lattice(
            self,
            tws0=tws0,
            file_name=file_name,
            remove_rep_drifts=remove_rep_drifts,
            power_supply=power_supply,
        )

    def transfer_maps(self, energy, output_at_each_step: bool = False):
        """
        Function calculates transfer maps, the first and second orders (R, T), for the whole lattice.

        :param energy: the initial electron beam energy [GeV]
        :param output_at_each_step: return three list of matrices [Bs], [Rs], [Ts] after each element in the line
        :return: B, R, T - matrices
        """
        Ra = np.eye(6)
        Ta = np.zeros((6, 6, 6))
        Ba = np.zeros((6, 1))
        Bs, Rs, Ts = [], [], []
        E = energy
        for elem in self.sequence:
            for Rb, Bb, Tb, tm in zip(elem.R(E), elem.B(E), elem.T(E), elem.tms):
                Ba, Ra, Ta = transfer_maps_mult(Ba, Ra, Ta, Bb, Rb, Tb)
                E += tm.get_delta_e()
                Bs.append(Ba)
                Rs.append(Ra)
                Ts.append(Ta)
        if output_at_each_step:
            return Bs, Rs, Ts
        return Ba, Ra, Ta


class EndElements:
    suffix_1 = "_1"
    suffix_2 = "_2"

    @staticmethod
    def check(lattice):
        pass

    @staticmethod
    def add(lattice):
        pass

    @staticmethod
    def update_first(end_element, body):
        pass

    @staticmethod
    def update_last(end_element, body):
        pass


def merge_drifts(cell):
    """
    Merge neighboring Drifts in one Drift

    :param cell: list of element
    :return: new list of elements
    """
    new_cell = []
    L = 0.0
    for elem in cell:
        if elem.__class__ in [Drift, UnknownElement]:
            L += elem.l
        else:
            if L != 0:
                new_elem = Drift(l=L)
                new_cell.append(new_elem)
            new_cell.append(elem)
            L = 0.0
    if L != 0:
        new_cell.append(Drift(l=L))
    print(
        "Merge drift -> Element numbers: before -> after: ",
        len(cell),
        "->",
        len(new_cell),
    )
    return new_cell


def exclude_zero_length_element(
    cell, elem_type=[UnknownElement, Marker], except_elems=[]
):
    """
    Exclude zero length elements some types in elem_type

    :param cell: list, sequence of elements
    :param elem_type: list, types of Elements which should be excluded
    :param except_elems: list, except elements
    :return: list, new sequence of elements
    """
    new_cell = []
    for elem in cell:
        if elem.__class__ in elem_type and elem.l == 0 and elem not in except_elems:
            continue
        new_cell.append(elem)
    print(
        "Exclude elements -> Element numbers: before -> after: ",
        len(cell),
        "->",
        len(new_cell),
    )
    return new_cell


def insert_markers_by_name(
    sequence, string: str, regex=False, before=True, after=True
) -> MarkersInsertionReturnType:
    """Insert markers either side of elements in the magnetic lattice, selected
    based on the element name (either equality or with a regular expression).
    By default markers are placed either side of the matched elements.

    :param string: Element string or regex string (with regex=True) to select
    elements to wrap with markers.
    :param regex: Whether to interpret argument `string` as a regex or not.  If
    not, then `string` is checked for equality against the element name.
    :param: Place a marker before each matched element.
    :param: Place a marker after each matched element.
    :return: Dictionary of element instances to list of (marker_start,
    marker_end pairs, like
    {element_instance: [(start1, start2), ... (startn, endn)]}.

    """
    if regex:

        def fre(ele):
            return bool(re.match(string, ele.id))

        return insert_markers_by_predicate(sequence, fre)

    def f(ele):
        return ele.id == string

    return insert_markers_by_predicate(sequence, f, before=before, after=after)


def insert_markers_by_type(
    sequence, magnet_type: Element, before=True, after=True
) -> MarkersInsertionReturnType:
    """Insert markers either side of elements in the magnetic lattice, selected
    based on the element
    By default markers are placed either side of the matched elements.

    :param string: Element string or regex string (with regex=True) to select
    elements to wrap with markers.
    :param: Place a marker before each matched element.
    :param: Place a marker after each matched element.
    :return: Dictionary of element instances to list of \
    (marker_start, marker_end pairs)
    """

    def f(ele):
        return isinstance(ele, magnet_type)

    return insert_markers_by_predicate(sequence, f, before=before, after=after)


def insert_markers_by_predicate(
    sequence, predicate: Callable[[Element], bool], before=True, after=True
) -> MarkersInsertionReturnType:
    """Insert markers either side of elements in the magnetic lattice, selected
    based on the the provided predicate function.

    :param predicate: Function on each element to select elements to wrap with
    markers.
    :param: Place a marker before each matched element.
    :param: Place a marker after each matched element.
    :return: Dictionary of element instances to list of \
    (marker_start, marker_end pairs)
    """

    indices = [i for (i, ele) in enumerate(sequence) if predicate(ele)]
    out_dict = defaultdict(list)
    for i in reversed(indices):
        ele = sequence[i]
        marker_before = None
        marker_after = None
        if after:
            marker_id_after = f"{ele.id}_after"
            marker_after = Marker(marker_id_after)
            sequence.insert(i + 1, marker_after)
        if before:
            marker_id_before = f"{ele.id}_before"
            marker_before = Marker(marker_id_before)
            sequence.insert(i, marker_before)

        out_dict[ele].append((marker_before, marker_after))

    return dict(out_dict)

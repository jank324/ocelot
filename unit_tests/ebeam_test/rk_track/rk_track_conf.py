"""Test parameters description file"""

import numpy as np
import pytest

from ocelot import *
from ocelot import RungeKuttaTM
from ocelot.cpbd.beam import generate_parray
from ocelot.cpbd.elements.undulator_atom import und_field

"""Lattice elements definition"""

d1 = Drift(l=0.1)
d2 = Drift(l=1)

und = Undulator(lperiod=0.4, nperiods=9, Kx=44.81, npoints=3000)
und.mag_field = lambda x, y, z: und_field(x, y, z, und.lperiod, und.Kx)
# und.npoints = 3000


"""pytest fixtures definition"""


@pytest.fixture(scope="module")
def cell():
    return (d1, und, d2)


@pytest.fixture(scope="module")
def method():
    m = {"global": SecondTM, Undulator: RungeKuttaTM}
    return m


@pytest.fixture(scope="module")
def lattice(cell, method):
    return MagneticLattice(cell, method=method)


@pytest.fixture(scope="function")
def p_array():
    np.random.seed(33)

    p_array = generate_parray(
        sigma_x=0,
        sigma_px=0,
        sigma_y=None,
        sigma_py=None,
        sigma_tau=100e-6 / 2.36,
        sigma_p=0,
        chirp=0.01 / 2.36,
        charge=0.5e-9,
        nparticles=10000,
        energy=0.6,
    )

    return p_array

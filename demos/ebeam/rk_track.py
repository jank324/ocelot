__author__ = "Sergey Tomin"

import copy

from ocelot import *
from ocelot.cpbd.beam import generate_parray
from ocelot.cpbd.elements.undulator_atom import und_field
from ocelot.gui.accelerator import *

d1 = Drift(l=0.1)
d2 = Drift(l=1)

und = Undulator(lperiod=0.4, nperiods=9, Kx=44.81, npoints=2000)
und.mag_field = lambda x, y, z: und_field(x, y, z, und.lperiod, und.Kx)


cell = (d1, und, d2)
method = {"global": SecondTM, "Undulator": RungeKuttaTM}

lat = MagneticLattice(cell, method=method)

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


p_array_1 = copy.deepcopy(p_array)

navi = Navigator(lat)
tws_track, p_array_1 = track(lat, p_array_1, navi, calc_tws=False)

plt.plot(p_array.tau() * 1000, p_array.p(), ".", label="initial distrib.")
plt.plot(p_array_1.tau() * 1000, p_array_1.p(), ".", label="after undul")
plt.legend()
plt.grid(True)
plt.show()

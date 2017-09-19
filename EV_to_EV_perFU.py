#

import numpy as np

nFU = 2.0

V, E = np.loadtxt('./calcite_II.dat').T

V_per_FU = V/nFU
E_per_FU = E/nFU

output_array = np.vstack((V_per_FU, E_per_FU)).T

np.savetxt('calcite_II_per_FU.dat', output_array, header="Volume per FU       Energy per FU", fmt="%0.13f")


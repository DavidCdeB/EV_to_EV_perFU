#

import numpy as np

V, E = np.loadtxt('./EL_vs_V.dat').T

# Lets assume V_eq = 57.6992532500000
# 100 - ((V_x - V_eq)/(V_eq) * 100)
V_eq = V[4]
print 'V[4] = ', V[4]

Percentage_volume = 100 + (((V - V_eq)/V_eq)*100)

output_array = np.vstack((V, Percentage_volume)).T

np.savetxt('V_Percentage_volume.dat', output_array, header="Volume     Percentage assuming V_eq = 57.69925325", fmt="%0.13f")

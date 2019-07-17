"""
PHYS 451 A6 Heat Capacity Per Dipole Plot
Rotating rod-shaped Molecules
"""

import numpy as np
import matplotlib.pyplot as plt

def heat_cap(T):
    return 2 - ( (1/T) / np.sinh(1/T) )**2

ax = plt.figure(figsize=(15,7)) # Set the plot size

# Label Plot
plt.xlabel("T (K)", fontsize='xx-large')
plt.ylabel("$C_{rot}$ (J/K)", fontsize='xx-large')
plt.title("Rotational Heat Capacity Per Dipole, $C_{rot}(T)$", fontsize='xx-large')
plt.grid(linestyle='dashed') # Add grid with solid lines to graph

T_vals = np.arange(0.01,2,1e-2)

plt.plot(T_vals, heat_cap(T_vals), linewidth=4
)
plt.xticks([1,2])
plt.yticks([1,2,3])
plt.xticks([0.5, 1, 1.5, 2],
           ["", "", "", ""])
plt.yticks([0.5, 1, 1.5, 2],
           ["", "", "", ""])

plt.axhline(y=0, color='k')
plt.axvline(x=0.001, color='k')

plt.ylim(-0.5,2.5)
plt.xlim(0,2)

plt.savefig('heatcapacity.png')
plt.show()
'''
Phys 451 - Assignment 3
Questions 9.9 and 9.10 from Statistical and Thermal Physics, H. Gould
Feb 19, 2019
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

# 9.19 Calculations

# import data
xdata = pd.read_csv('xdata.csv')
ydata = pd.read_csv('ydata.csv')

# Isolate floats
xdata = xdata.values
ydata = ydata.values

# Convert to list
x_s = [x[0] for x in xdata]
y_s = [y[0] for y in ydata]

def my_func(x, A, t):
    '''
    Function defines the expected power law relationship b/w x and y
    '''
    return A*x**(-t)

ax = plt.figure(figsize=(15,7)) # Set the plot size

# Label Plot
plt.xlabel("Mean Number of Clusters of size $s$ ()", fontsize='x-large')
plt.ylabel("Cluster Size Distribution $<n_s> ()$", fontsize='x-large')
plt.title("Cluster Size Distribution $p=0.5927$, $L=128$", fontsize='xx-large')

plt.grid(linestyle='dashed') # Add grid with solid lines to graph

plt.scatter(x_s,y_s, label='Data', s=6)

popt, pcov = curve_fit(my_func, x_s, y_s)
plt.loglog(x_s, my_func(x_s, *popt), label='Fit to All Data', lw=5, ls='--', c='r')

popt1, pcov1 = curve_fit(my_func, x_s[10:], y_s[10:])
plt.loglog(x_s, my_func(x_s, *popt1), label='Fit Omit First 10', lw=5, ls=':', c='m')

plt.ylim(10**-3,10**2)

# Add customized legend
legend = plt.legend(loc=0, fontsize='x-large', shadow=(True), borderaxespad=3)
frame = legend.get_frame()
frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6)

plt.savefig('LogPlot.png')
plt.show()

print('Calculated Coefficients for Fit to All Data, (A,t):\n\t', popt)
print('Calculated Coefficients for Fit Omitting First 10 Data Points, (A,t):\n\t', popt1)

# 9.10 Calculations

L1 = [10,20,40,80]
Pinf = [0.49, 0.41, 0.358, 0.307]

def power1(L, A, greek):
    '''
    Pinfty power law
    '''
    return A*L**(-greek)

ax = plt.figure(figsize=(15,7)) # Set the plot size

# Label Plot
plt.xlabel("Lattice Size, $L$ ()", fontsize='x-large')
plt.ylabel("Order Parameter, $P_\infty$ ()", fontsize='x-large')
plt.title("Power Law Relationship between Order Parameter and Lattice Size", fontsize='xx-large')

plt.scatter(L1, Pinf, marker='*', c='r')

popt, pcov = curve_fit(power1, L1, Pinf)
plt.loglog(L1, power1(L1, *popt)) #, lw=5, ls='--', c='r'

plt.savefig('Pinfty.png')
plt.show()

print('Calculated Coefficients, (A, greek):\n\t', popt)

S = [13.907, 38.478, 154.364, 443.088]

def power2(L, A, greek):
    '''
    S power law
    '''
    return A*L**(greek)

ax = plt.figure(figsize=(15,7)) # Set the plot size

# Label Plot
plt.xlabel("Lattice Size, $L$ ()", fontsize='x-large')
plt.ylabel("Mean Size of Finite Clusters, $S$ ()", fontsize='x-large')
plt.title("Power Law Relationship between Finite Cluster and Lattice Sizes", fontsize='xx-large')

plt.scatter(L1, S, marker='*', c='r')

popt, pcov = curve_fit(power2, L1, S)
plt.loglog(L1, power2(L1, *popt))

plt.savefig('S.png')
plt.show()

print('Calculated Coefficients, (A, greek):\n\t', popt)

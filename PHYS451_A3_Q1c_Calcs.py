'''
Phys 451 - Assignment 3 Question 9.19 Calculations
Feb 19, 2019
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

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

print(popt)
print(popt1)
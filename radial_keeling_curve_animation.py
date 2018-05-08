import numpy as np

# Retrieve the columns of data in the text file
# Sourced from: ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt
filename = 'co2_mm_mlo.txt'
data = np.genfromtxt( filename, skip_header=72, max_rows=792, usecols=(0,1,2,3,4,5), 
                     names=['year', 'month', 'ddate', 'average','interpolated', 'trend'] )

def yearly_average(array):
    
    yrly_avgs = []
    i = 0
    months = 12
    list_pos = 0
    
    while ( i < len(data)/months ):
        summation = 0
        for reading in array[list_pos:list_pos+months]:
            summation += reading
        i += 1
        list_pos += months
        yrly_avgs.append(summation/months)
    
    return yrly_avgs

yearly_averages = yearly_average(data['trend'])
years = np.arange(1958, 2018, 1)

from matplotlib import pyplot as plt
from matplotlib import animation
from IPython.display import HTML

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(figsize=(15,10))
ax = plt.axes(polar=True)
ax.set_ylim(310,400)
line, = ax.plot([], [], lw=2)
title = ax.text (0.02, 1.0, 'TITLE', fontsize=14, transform=ax.transAxes)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    title.set_text ('NOPE')
    return line, title

# animation function.  This is called sequentially
def animate(i):
    theta = np.arange(0,2.1*np.pi, 0.1)
    r = np.array([0])*len(theta)+i
    line.set_data(theta, r)
    title.set_text (i.__str__())
    return line

# call the animator.  blit=True means only re-draw the parts that have changed.
'''
for msmt in yearly_averages:
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=60, interval=20, blit=False, fargs=(msmt,))
    HTML(anim.to_jshtml())
'''
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=yearly_averages, interval=200, 
                               blit=False, repeat=False)
HTML(anim.to_jshtml())
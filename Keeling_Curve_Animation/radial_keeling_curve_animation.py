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
select_data = [i for i in zip(yearly_averages, years)] 

from matplotlib import pyplot as plt
from matplotlib import animation
from IPython.display import HTML


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(figsize=(15,10))
fig.suptitle('$CO_2$ Concentration at Mauna Loa Observatory, Hawaii', fontsize=20)
ax = plt.axes(polar=True)
ax.set_ylim(310,500)
line, = ax.plot([], [], lw=2)
title = ax.text (0.02, 1.0, '', fontsize=16, transform=ax.transAxes)
title1 = ax.text(0.02, 0.0, '', fontsize=16, transform=ax.transAxes)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line

# animation function.
def animate(i):
    theta = np.arange(0,2.1*np.pi, 0.1)
    r = np.array([0])*len(theta)+i[0]
    line.set_data(theta, r)
    title.set_text ('Year: ' + i[1].__str__())
    title1.set_text ('CO2: ' + np.round(i[0], 2).__str__() + ' ppm')
    return line

# call the animator.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=select_data, interval=200, blit=False, repeat=True)
HTML(anim.to_jshtml())
#anim.save('keeling_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
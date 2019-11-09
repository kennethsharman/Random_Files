'''
Code used in PHYS 597 Lab #2: Michelson Fourier Transform Spectroscopy
Date:   November 8, 2019
Author: Kenneth Sharman
'''
# import required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import scipy.signal

# Import HeNe laser data set
laser_data = np.genfromtxt('ds2_laser.dat', delimiter=',')
assert len(laser_data) == 30000

# empty arrays to store votage and time data
voltage, time = [], []

# store the votlage and time data separately
for i in range(len(laser_data)):
    voltage.append((laser_data[i][2]))
    time.append(laser_data[i][1])

def crop_data(arr, target_index, len_crop):
    '''Function crops an array to len_crop, centered about target_index
    and returns the cropped array'''
    half_crop = len_crop//2
    first_half = arr[target_index-half_crop : target_index]
    second_half = arr[target_index : target_index+half_crop]
    x_start_index = target_index-half_crop
    return (np.concatenate((first_half, second_half)), x_start_index)

# size of fourier transform
N = 1024*4

total_list = [] # array used to store overlapping, windowed, array
window = scipy.signal.blackmanharris(N) # window used for HeNe fourier transform

# crop and overlap windowed array
for i in range(10):
    temp, __ = crop_data(voltage, len(voltage)//2 + (i*100) + 4550, N) #4096
    total_list.append( temp * window )
    
# array to store fft
total_fft = np.zeros(N, dtype=complex)

# take fft of overlapping datasets
for i in range(len(total_list)):
    total_fft += np.conj(fft(total_list[i]))*fft(total_list[i])
total_fft_half = total_fft[:len(total_fft)//2].real

print(np.argmax(total_fft_half)) # bin of peak
wl_vals = [] # wavelength array

# motor speed
v = 500000/(3*60+59) # nm/s

# get the wavelength array.
# 100 samples per second
for i in range(len(total_fft_half)):
    if i == 0 : wl_vals.append(0)
    else: wl_vals.append(  (2*v*len(total_fft_half))/(50*(i)) )
        
# find peaks of fft
peaks, info = scipy.signal.find_peaks(total_fft_half, distance = 10000, width=2, rel_height=0.5)
assert len(peaks) == 1

# normalize fft by the max intensity
max_intensity = total_fft_half[peaks[0]]
for i in range(len(total_fft_half)):
    total_fft_half[i] /= max_intensity  
    
# plot HeNe fft
ax = plt.figure(figsize=(15, 9)); plt.style.use('seaborn') # print(plt.style.available)

plt.plot(wl_vals[1:], total_fft_half[1:], lw=5, zorder=0, c='k', label='Michelson Interferometer')
plt.vlines(632.9, -0., 1.05, colors='r', linestyles='--', lw=4, zorder=10, label='$\lambda = 632.9\,nm$')

plt.xlim(wl_vals[peaks[0]]-100,wl_vals[peaks[0]]+100)
plt.xlabel('Wavelength ($nm$)', fontsize='30', labelpad=20)
plt.ylabel('Normalized Intensity', fontsize='30', labelpad=20)
plt.grid(linestyle='dashed')
legend = plt.legend(loc=1, shadow=(True), prop={'size': 25})
frame = legend.get_frame()
frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6)
plt.tick_params(labelsize=25)
#plt.savefig('laser.png')

# 
print('HeNe Peak Wavelength =', wl_vals[peaks[0]])
print('HeNe Peak Wavelength FWHM =', (2*v*len(total_fft)//2)/(50*info['left_ips'][0]) \
      - (2*v*len(total_fft)//2)/(50*info['right_ips'][0]))

# shift fft by correction value
correction = 632.8 / wl_vals[peaks[0]]


# Import Mercury Lamp data
mercury_data = np.genfromtxt('ds3_mercury.dat', delimiter=',')
assert len(mercury_data) == 30000

# store voltage and time data of mercury lamp measurements separately
voltage2, time2 = [], []

for i in range(len(mercury_data)):
    voltage2.append((mercury_data[i][2]))
    time2.append(mercury_data[i][1])
    
'''Mercury lamp fft section'''
N2, starting = 1024*4, 10935
space = N2//2
wl_vals2, total_list2 = [], []
total_fft2 = np.zeros(space, dtype=complex)
temp2, x_start = crop_data(voltage2, starting, space)

'''Select appropriate window'''
#window2 = scipy.signal.blackmanharris(space); plot_window = scipy.signal.blackmanharris(51)
#window2 = scipy.signal.gaussian(space, 250); plot_window = scipy.signal.gaussian(51, 250)
#window2 = scipy.signal.nuttall(space); plot_window = scipy.signal.nuttall(51)
window2 = scipy.signal.parzen(space); plot_window = scipy.signal.parzen(51)
#window2 = scipy.signal.slepian(space,0.01); plot_window = scipy.signal.slepian(51, 0.01)

'''This section computes fft of Mercury lamp data and also wavelenth array'''

for i in range(2):
    temp2, __ = crop_data(voltage2, starting+(i*1024), space)
    total_list2.append( temp2 * window2 )

for i in range(len(total_list2)):
    total_fft2 += np.conj(fft(total_list2[i]))*fft(total_list2[i])
total_fft_half2 = total_fft2[:len(total_fft2)//2].real

for i in range(len(total_fft_half2)):
    if i == 0 : wl_vals2.append(0)
    else: wl_vals2.append(  correction * (2*v*len(total_fft_half2))/(50*(i)) )   

max_intensity2 = total_fft_half2[np.argmax(total_fft_half2)]
for i in range(len(total_fft_half2)):
    total_fft_half2[i] /= max_intensity2

spectrum = [296.7, 313.2, 365.0, 404.7, 435.8, 546.1, 579.1, 1014.0]
for wl in spectrum:
    filtered = np.copy(total_fft_half2)
    for i in range(len(filtered)):
        if np.abs(wl_vals2[i]-wl)>(0.015*wl):
            filtered[i] = 0
    peak, info = scipy.signal.find_peaks(filtered, distance = 5,  width=2, rel_height=0.5)
    if len(peak)>0:
        print('*******************************')
        print('Expected =', wl)
        print('Wavelength : %15.1f' % wl_vals2[peak[0]])
        
        FWHM = ((2*v*len(filtered))/(50*info['left_ips'][0]) \
              - (2*v*len(filtered))/(50*info['right_ips'][0]))
        print('Within FWHM :         ', (np.abs(wl-wl_vals2[peak[0]]) < FWHM))
        print('FWHM : %19.1f' % FWHM)
        print('Relative Uncertainty : %4.2f' % (100*FWHM / wl_vals2[peak[0]]) )
    else:
        print('\n*******************************ERROR on wavelength =',wl, '\n')

'''Plot Mercury lamp fft'''
        
ax = plt.figure(figsize=(15, 7))

# uncomment if you want lines for each expected wavelength
#for line in spectrum:
#    plt.vlines(line, 0.1, 1.05, colors='blue', linestyles='--', lw=4, zorder=10)
plt.plot(wl_vals2[1:], total_fft_half2[1:], lw=3, zorder=10, c='k')

plt.xlim(200,1100)
plt.xlabel('Wavelength ($nm$)', fontsize='20', labelpad=20)
plt.ylabel('Normalized Intensity', fontsize='20', labelpad=20)
plt.grid(linestyle='dashed')
plt.tick_params(labelsize=15)
#plt.savefig('merc.png')
plt.show()

ax = plt.figure(figsize=(15, 9))
plt.plot(time2[x_start:x_start+len(temp2)], temp2*0.6, c='steelblue')
plt.plot(time2[x_start:x_start+len(temp2)], temp2*window2, c='r')
plt.plot(time2[x_start:x_start+len(temp2)], window2*4.17, c='k', ls='--', lw=3)
plt.xlabel('Time ($ms$)', fontsize='30', labelpad=20)
plt.ylabel('Voltage (V)', fontsize='30', labelpad=20)
plt.grid(linestyle='dashed')
plt.tick_params(labelsize=25)
#plt.savefig('wave.png')
plt.show()

from scipy.fftpack import fft, fftshift
A = fft(plot_window, 2048) / (len(plot_window)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
ax = plt.figure(figsize=(15, 4)); plt.plot(freq, response)
plt.axis([-0.5, 0.5, -120, 0])
plt.title("Frequency response of the window")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]"); plt.show()
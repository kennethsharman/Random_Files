'''
Code used in PHYS 597 Lab #3: Pulsed NMR Spectroscopy
Date:   November 30, 2019
Author: Kenneth Sharman
'''
# import required packages 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import optimize

# import data
ds2 = np.genfromtxt('ds2.csv', delimiter=',')
ds3 = np.genfromtxt('ds3.csv', delimiter=',')
ds4 = np.genfromtxt('ds4.csv', delimiter=',')
ds5 = np.genfromtxt('ds5.csv', delimiter=',')

def T1_model(t, M0, T1):
    return M0*(1.0-2.0*np.exp(-t/T1))

def T2_model(t, M0, T2):
    return M0*np.exp(-2*t/T2)

# MO == mineral oil
MO_T1_delays = ds2[0]
MO_T1_voltages = ds2[1]

MO_T1_popt, MO_T1_pcov = curve_fit(T1_model, MO_T1_delays, MO_T1_voltages, p0=[3.0, 21])
print('Mineral Oil (T1):\n\tM0 =', MO_T1_popt[0], '\n\tT1 =', MO_T1_popt[1])

sol = optimize.root(T1_model, [21], args=(MO_T1_popt[0], MO_T1_popt[1]), method='hybr')
print('Root:\t x =', sol.x[0])

MO_M0_Z = str(np.round(MO_T1_popt[0], 1))
MO_T1 = str(int(np.round(MO_T1_popt[1], 0)))

print('u(M0) =', np.round(0.05*MO_T1_popt[0], 1))
print('u(T1) =', np.round(0.05*MO_T1_popt[1], 0))

ax = plt.figure(figsize=(12, 8)); plt.grid(linestyle='dashed')
plt.title('Mineral Oil - T1', fontsize='30', y=1.03)
plt.xlabel('Delay Time ($ms$)', fontsize='20', labelpad=20)
plt.ylabel('Voltage (V)', fontsize='20', labelpad=20)

plt.scatter(MO_T1_delays, MO_T1_voltages, label='Data')
plt.plot(MO_T1_delays, T1_model(MO_T1_delays, *MO_T1_popt ),\
         label='Fit: $M_z(0) =$' + MO_M0_Z + ', $T1=$' + MO_T1 + ' $ms$ ', c='r') 

legend = plt.legend(loc=4, shadow=(True), prop={'size': 20})
frame = legend.get_frame(); frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6); plt.tick_params(labelsize=15)
plt.show()

MO_T2_delays = ds3[0]
MO_T2_voltages = ds3[1]

MO_T2_popt, MO_T2_pcov = curve_fit(T2_model, MO_T2_delays, MO_T2_voltages, p0=[3.5, 25])
print('Mineral Oil (T2):\n\tM0 =', MO_T2_popt[0], '\n\tT2 =', MO_T2_popt[1])

MO_M0_XY = str(np.round(MO_T2_popt[0], 1))
MO_T2 = str(int(np.round(MO_T2_popt[1], 0)))

print('u(M0) =', np.round(0.05*MO_T2_popt[0], 1))
print('u(T2) =', np.round(0.05*MO_T2_popt[1], 0))

ax = plt.figure(figsize=(12, 8)); plt.grid(linestyle='dashed')
plt.title('Mineral Oil - T2', fontsize='30', y=1.03)
plt.xlabel('Delay Time ($ms$)', fontsize='20', labelpad=20)
plt.ylabel('Voltage (V)', fontsize='20', labelpad=20)

plt.scatter(MO_T2_delays, MO_T2_voltages, label='Data')
plt.plot(MO_T2_delays, T2_model(MO_T2_delays, *MO_T2_popt ),\
         label='Fit: $M_{xy}(0)=$' + MO_M0_XY + ', $T2=$' + MO_T2 + '$\,ms$ ', c='r') 

legend = plt.legend(loc=1, shadow=(True), prop={'size': 20})
frame = legend.get_frame(); frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6); plt.tick_params(labelsize=15)
plt.show()

# GLYC == glycerine
GLYC_T1_delays = ds4[0]
GLYC_T1_voltages = ds4[1]

GLYC_T1_popt, GLYC_T1_pcov = curve_fit(T1_model, GLYC_T1_delays, GLYC_T1_voltages, p0=[3.0, 17])
print('Glycerine (T1):\n\tM0 =', GLYC_T1_popt[0], '\n\tT1 =', GLYC_T1_popt[1])

sol = optimize.root(T1_model, [17], args=(GLYC_T1_popt[0], GLYC_T1_popt[1]), method='hybr')
print('Root:\t x =', sol.x[0])

GLYC_M0_Z = str(np.round(GLYC_T1_popt[0], 1))
GLYC_T1 = str(int(np.round(GLYC_T1_popt[1], 0)))

print('u(M0) =', np.round(0.05*GLYC_T1_popt[0], 1))
print('u(T1) =', np.round(0.05*GLYC_T1_popt[1], 0))

ax = plt.figure(figsize=(12, 8)); plt.grid(linestyle='dashed')
plt.title('Glycerine - T1', fontsize='30', y=1.03)
plt.xlabel('Delay Time ($ms$)', fontsize='20', labelpad=20)
plt.ylabel('Voltage (V)', fontsize='20', labelpad=20)

plt.scatter(GLYC_T1_delays, GLYC_T1_voltages, label='Data')
plt.plot(GLYC_T1_delays, T1_model(GLYC_T1_delays, *GLYC_T1_popt ),\
         label='Fit: $M_z(0) =$' + GLYC_M0_Z + ', $T1=$' + GLYC_T1 + ' $ms$ ', c='r') 

legend = plt.legend(loc=4, shadow=(True), prop={'size': 20})
frame = legend.get_frame(); frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6); plt.tick_params(labelsize=15)
plt.show()

GLYC_T2_delays = ds5[0]
GLYC_T2_voltages = ds5[1]

GLYC_T2_popt, GLYC_T2_pcov = curve_fit(T2_model, GLYC_T2_delays, GLYC_T2_voltages, p0=[3.5, 25])
print('Glycerine (T2):\n\tM0 =', GLYC_T2_popt[0], '\n\tT2 =', GLYC_T2_popt[1])

GLYC_M0_XY = str(np.round(GLYC_T2_popt[0], 1))
GLYC_T2 = str(int(np.round(GLYC_T2_popt[1], 0)))

print('u(M0) =', np.round(0.05*GLYC_T2_popt[0], 1))
print('u(T2) =', np.round(0.05*GLYC_T2_popt[1], 0))

ax = plt.figure(figsize=(12, 8)); plt.grid(linestyle='dashed')
plt.title('Glycerine - T2', fontsize='30', y=1.03)
plt.xlabel('Delay Time ($ms$)', fontsize='20', labelpad=20)
plt.ylabel('Voltage (V)', fontsize='20', labelpad=20)

plt.scatter(GLYC_T2_delays, GLYC_T2_voltages, label='Data')
plt.plot(GLYC_T2_delays, T2_model(GLYC_T2_delays, *GLYC_T2_popt ),\
         label='Fit: $M_{xy}(0)=$' + GLYC_M0_XY + ', $T2=$' + GLYC_T2 + '$\,ms$ ', c='r') 

legend = plt.legend(loc=1, shadow=(True), prop={'size': 20})
frame = legend.get_frame(); frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6); plt.tick_params(labelsize=15)
plt.show()

# Recap
print('****** MINERAL OIL ******')
print('\tT1 =', MO_T1, ' ms')
print('\tT2 =', MO_T2, ' ms')
print('\n')
print('****** GLYCERINE ******')
print('\tT1 =', GLYC_T1, ' ms')
print('\tT2 =', GLYC_T2, ' ms')

fig = plt.figure(figsize=(16,8))

ax1 = plt.subplot(1,2,1); plt.grid(linestyle='dashed')
ax1.text(0, 3.65, '[A]', fontsize=35)
plt.title('Mineral Oil', fontsize='25', y=1.03)
plt.xlabel('Delay Time ($ms$)', fontsize='20', labelpad=20)
plt.ylabel('Voltage (V)', fontsize='20', labelpad=20)
plt.tick_params(labelsize=15)

plt.errorbar(MO_T1_delays, MO_T1_voltages, yerr=MO_T1_voltages*0.05, label='Data', zorder=3,\
           uplims=True, lolims=True, fmt='o')
plt.plot(MO_T1_delays, T1_model(MO_T1_delays, *MO_T1_popt ),\
         label='Fit: $M_{z}(0)=$' + MO_M0_Z + '(2) A/m\n      $T_1=$' + MO_T1 + '(2) ms ', c='r', lw=5) 

legend = plt.legend(loc=4, shadow=(True), prop={'size': 20})
frame = legend.get_frame(); frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6); plt.tick_params(labelsize=15)

ax2 = plt.subplot(1,2,2); plt.grid(linestyle='dashed')
ax2.text(0, 3.35, '$[B]$', fontsize=35)
plt.title('Glycerine', fontsize='25', y=1.03)
plt.xlabel('Delay Time ($ms$)', fontsize='20', labelpad=20)
plt.ylabel('Voltage (V)', fontsize='20', labelpad=20)
plt.tick_params(labelsize=15)

plt.errorbar(GLYC_T1_delays, GLYC_T1_voltages, yerr=0.05*GLYC_T1_voltages,\
             label='Data', zorder=3, uplims=True, lolims=True, fmt='o')
plt.plot(GLYC_T1_delays, T1_model(GLYC_T1_delays, *GLYC_T1_popt ),\
         label='Fit: $M_{z}(0)=$' + GLYC_M0_Z + '(2) A/m\n      $T_1=$' + GLYC_T1 + '(1) ms ', c='r', lw=5) 

legend = plt.legend(loc=4, shadow=(True), prop={'size': 20})
frame = legend.get_frame(); frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6); plt.tick_params(labelsize=15)

plt.subplots_adjust(wspace=0.3)
#plt.savefig('t1_results.png')
plt.show()

fig = plt.figure(figsize=(16,8))

ax1 = plt.subplot(1,2,1); plt.grid(linestyle='dashed')
ax1.text(0, 3.45, '[A]', fontsize=35)
plt.title('Mineral Oil', fontsize='25', y=1.03)
plt.xlabel('Delay Time ($ms$)', fontsize='20', labelpad=20)
plt.ylabel('Voltage (V)', fontsize='20', labelpad=20)
plt.tick_params(labelsize=15)

plt.errorbar(MO_T2_delays, MO_T2_voltages, yerr=0.05*MO_T2_voltages, label='Data', zorder=3,\
           uplims=True, lolims=True, fmt='o')
plt.plot(MO_T2_delays, T2_model(MO_T2_delays, *MO_T2_popt ),\
         label='Fit: $M_{xy}(0)=$' + MO_M0_XY + '(2) A/m \n      $T_2=$' + MO_T2 + '(1) ms ', c='r', lw=5) 
legend = plt.legend(loc=1, shadow=(True), prop={'size': 20})
frame = legend.get_frame(); frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6); plt.tick_params(labelsize=15)

ax2 = plt.subplot(1,2,2); plt.grid(linestyle='dashed')
ax2.text(0, 3., '$[B]$', fontsize=35)
plt.title('Glycerine', fontsize='25', y=1.03)
plt.xlabel('Delay Time ($ms$)', fontsize='20', labelpad=20)
plt.ylabel('Voltage (V)', fontsize='20', labelpad=20)
plt.tick_params(labelsize=15)

plt.errorbar(GLYC_T2_delays, GLYC_T2_voltages, yerr=GLYC_T2_voltages*0.05, label='Data', zorder=3,\
            uplims=True, lolims=True, fmt='o')
plt.plot(GLYC_T2_delays, T2_model(GLYC_T2_delays, *GLYC_T2_popt ),\
         label='Fit: $M_{xy}(0)=$' + GLYC_M0_XY + '(2) A/m \n      $T_2=$' + GLYC_T2 + '(1) ms', c='r', lw=5) 
legend = plt.legend(loc=1, shadow=(True), prop={'size': 20})
frame = legend.get_frame(); frame.set_facecolor('#f9f9f9')
frame.set_alpha(0.6); plt.tick_params(labelsize=15)

plt.subplots_adjust(wspace=0.3)
#plt.savefig('t2_results.png')
plt.show()

# -*- coding: utf-8 -*-
"""
Connect Bluetooth Arduino to Python on desktop
Created on Fri Jul  5 19:08:23 2019
@author: Ken (Python 3.6)
"""

import serial
import time
print("Start")
#ser1 = serial.Serial('COM3', baudrate = 9600, timeout=1);

ser1 = serial.Serial('COM5', baudrate = 9600, timeout=1);
i = 0

#print(ser1.is_open)
#print(ser1.read_all())
while i<10:
    read_val = ser1.read(100)
    print(read_val)
    i += 1
ser1.close()

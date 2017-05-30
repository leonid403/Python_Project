# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from src.signal import Signal
from src.spectrum import Spectrum

SA = '10.18.134.187'
SG = '10.18.134.209'

dev1 = Signal(SG)
dev2 = Spectrum(SA)
dev1.visa_open()
dev2.visa_open()
print(dev1.info())
print(dev2.info())
dev1.preset()
dev2.preset()

dev1.set_amp(-10)
dev1.set_rf_on_off('ON')
dev2.set_span(50e6)
dev2.set_mark_on_off('ON')

start = 10e9
stop = 20e9
npts = 21
freq = np.linspace(start, stop, npts)
mark = []
for i in freq:
    time.sleep(0.2)
    dev1.set_freq(i)
    time.sleep(0.1)
    dev2.set_freq(i)
    time.sleep(0.2)
    dev2.set_mark_freq(i)
    time.sleep(0.2)
    #    print dev2.get_mark_freq()
    mark.append(dev2.get_mark_freq())

dev1.visa_close()
dev2.visa_close()
plt.plot(freq, mark)
plt.grid()
plt.show()
# print (sg.get_amp())

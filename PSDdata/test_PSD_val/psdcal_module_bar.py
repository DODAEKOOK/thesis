# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:43:20 2016

@author: ddk13
"""
from numpy import *
from scipy.signal import *
from numpy.fft import * 
from scipy import *
from pylab import *
import matplotlib.pyplot as plt
from scipy.fftpack import rfft, irfft, fftfreq


f=open('KJH_14_after_r_gch.txt','r')

chno = 8   # total number of channels
eeg = []

while True:
 testline = f.readline()
 if len(testline) == 0:
  break #EOF
 testline = testline.split()
 eeg.append([])
 for i in xrange(0,chno):
  eeg[-1].append(float(testline[i]))

ch = 0 # particualr channel to study
eeg = array(eeg)
y = eeg[:,ch]         # the signal, study channel 'ch'
L = len(y)            # signal length
fs = 250.0              # sampling rate
T = 1/fs                # sample time
#Y = fft(y)

figure()
filtered = []
b= [] # store filter coefficient
cutoff = [0.5,4.0,8,13,30.0]

for band in xrange(0, len(cutoff)-1):
 wl = 2*cutoff[band]/fs*pi
 wh = 2*cutoff[band+1]/fs*pi
 M = 512      # Set number of weights as 128
 bn = zeros(M)

 for i in xrange(0,M):     # Generate bandpass weighting function
  n = i-  M/2       # Make symmetrical
  if n == 0:
   bn[i] = wh/pi - wl/pi;
  else:
   bn[i] = (sin(wh*n))/(pi*n) - (sin(wl*n))/(pi*n)   # Filter impulse response

 bn = bn*kaiser(M,5.2)  # apply Kaiser window, alpha= 5.2
 b.append(bn)

 [w,h]=freqz(bn,1)
 filtered.append(convolve(bn, y)) # filter the signal by convolving the signal with filter coefficients

#Y = filtered[2]


signal = y
time   = np.linspace(0,10,2000)
W = fftfreq(signal.size, d=time[1]-time[0])
f_signal = rfft(signal)

# If our original signal time was in seconds, this is now in Hz
cut_f_signal = f_signal.copy()
cut_f_signal[(W<13)] = 0
cut_f_signal[(W>20.5)] = 0

cut_signal = irfft(cut_f_signal)


# Compute PSD
S_mlab, f_mlab = mlab.psd(
    cut_signal, Fs=fs, NFFT=1024, noverlap=(125),
    detrend=None, scale_by_freq=True, window=mlab.window_hanning)

plt.close()

sum_alpha_band_value = 0
avr_alpha_band_value = 0

for k in range(21):
    sum_alpha_band_value = sum_alpha_band_value + S_mlab[k+33] # 33 34 ... 53


avr_alpha_band_value = sum_alpha_band_value/21

print(f_mlab[33:54])

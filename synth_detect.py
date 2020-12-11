import numpy as np
import matplotlib.pyplot as plt

def synth_detect(data,smpl_rate):
    hz = smpl_rate
    signal = data[:,1] # gets chord sine wave data
    N = (len(signal)) # establishes number 
    freq_data = np.abs(np.fft.fft(signal))/N # gets y axis values for intensity vs freq
    freq_data = freq_data[0:int(N/2)] # cuts data off at Nyquest limit
    v = np.arange(int(N/2))
    tau = N/hz
    f = v/tau # establishes freq bins
    return   [f,freq_data]


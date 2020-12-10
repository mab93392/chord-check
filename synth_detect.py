import numpy as np
from chord import Chord
import matplotlib.pyplot as plt

def synth_detect(data,smpl_rate):
    hz = smpl_rate
    signal = data[:,1]
    N = (len(signal))
    freq_data = np.abs(np.fft.fft(signal))/N
    freq_data = freq_data[0:int(N/2)]
    v = np.arange(int(N/2))
    tau = N/hz
    f = v/tau
    return   [f,freq_data]

# chord = Chord()
# data = chord.final_out()[0]
# a = synth_detect(data,44100)
# print(a)
# print(len(a[0]))
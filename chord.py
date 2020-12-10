import numpy as np
import multiprocessing as mp
from name import name
from chord_tone import chord_tone
from calc_waveform import calc_waveform
class Chord:


    def __init__(self):
        
        self.deg = np.random.randint(0,11) # random picks numerical key option
        self.key = (440 / np.power(2,7)) * (1+2*self.deg/12) # generates fundemental frequency for the
                                                             # the series of frequencies that make up chord
        
        self.key_name = name(self.deg) # converts numerical chord option to text ouput
        self.O = np.random.randint(0,27)
    # Generates series of frequencies with arbitrary intensity units that peak in the middle 
    # of range of frequencies 
    def data_gen(self,O):

        return chord_tone(O,self.key)

    # Takes the previously generated series of frequencies and computes a weighted sum
    # of sin waves with those frequences at time points increasing in 
    # time incriments of 1/50,000 of a second. The wieghts the respective intensities of the 
    # frequencies. The "n" allows for multiple time intervals to be used, that allows parallel 
    # processing.
    def wave(self,n,O):
        data = self.data_gen(O)
        a = data[0]
        b = data[1]
        c = data[2]
        d = data[3]
        return [calc_waveform(a,n),b,c,d]

    # Reduces number of inputs for wave function down to 1. This allows for the pool.map
    # method of parallel proccessing.
    def mp_wave(self,n): 
        
        
        return self.wave(n,self.O)
    
    # outputs all germane data in concise function
    def final_out(self):
        
        pool = mp.Pool(mp.cpu_count())
        calc = pool.map(self.mp_wave,[1,2,3,4])
        t_vs_y = [calc[0][0],calc[1][0],calc[2][0],calc[3][0]]
        t_vs_y = np.reshape(t_vs_y, (4*len(calc[0][0]),2))
        chord_name = [self.key_name + " " + calc[0][1] + "/" + calc[0][2]]
        out = [t_vs_y,chord_name,self.deg,self.O,calc[3][3]]
        return np.array(out, dtype=object)
    






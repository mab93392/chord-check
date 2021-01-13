import numpy as np

def degrees(key,deg):
    deg_num = len(deg)
    freqs = []
    I = []

    for i in range(0,deg_num):
        for n in range(0,11):
            
            k = np.power(2,n) # octave multiplier
            c_key = key*k # first note of octave
            if deg[i] == 0:
                freqs = np.append(freqs,c_key) # adds first note of ocatave
            else:
                freqs = np.append(freqs,deg[i]*c_key*2/12) # adds subsequent notes of chord
            
            
            for j in range(0,(deg_num-1)):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5)) # adds decay-from-middle-range term
                t2 = (1 / (1+np.exp(-xx))) / 3 # adds noise term
                I = np.append(I,(t1+t2) / 2 ) # combines terms and adds them to intensity list

    freqs = np.reshape(freqs,(len(freqs),1))
    I = np.reshape(freqs,(len(I),1))
    tone_data = np.append(freqs,I,1)

    return tone_data



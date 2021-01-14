import numpy as np

def inversions(key):
    A_base = 440/np.power(2,6) # generates fundemental base pitch for series of base frequencies
    base_opt = np.random.randint(0,11) # randomly picks inversion

    if key == 0:
        A_base = 0
    
    base_pitch = []
    
    inv = []
    I = []

    for n in range(0,4):
        c_base = np.power(2,n)*A_base
        if base_opt == 0:
            base_pitch = np.append(base+pitch,c_base)
        else:
            base_pitch = np.append(base_pitch,(base_opt*2*c_base/12)) # adds base pitch

        # L = len(base_pitch)

        for i in range(0,1):                                        # makes mid-base range peaking 
                    xx = np.random.rand()                           # intensities with random noise
                    c1 = (1 / (1 + np.exp(-xx))) 
                    c2 = abs(1/ (n-2.2))
                    I = np.append(I, (c2 + c1 ) / 5)

    I = np.reshape(I,(len(I),1))
    base_pitch = np.reshape( base_pitch, (len(base_pitch),1))
    base_freqs = np.append(base_pitch,I,1)

    if base_opt == 0:           # assigns text to random inversion option 
        inv = "A"
    elif base_opt == 1:
        inv = "A#"
    elif base_opt == 2:
        inv = "B"
    elif base_opt == 3:
        inv = "C"
    elif base_opt == 4:
        inv = "C#"
    elif base_opt == 5:
        inv = "D"
    elif base_opt == 6:
        inv = "D#"
    elif base_opt == 7:
        inv = "E"
    elif base_opt == 8:
        inv = "F"
    elif base_opt == 9:
        inv = "F#"
    elif base_opt == 10:
        inv = "G"
    elif base_opt == 11:
        inv = "G#"


    return [base_freqs,inv,base_opt]
    



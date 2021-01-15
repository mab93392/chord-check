from inversions import inversions
import numpy as np
from degrees import degrees


# Each conditional represents different chord type.


def chord_tone(x,key):
    Type = []
    type_ = x
    I = []
    freqs = []

    if type_ == 0: # major triad
        Type = "major triad"
        tone_data = degrees(key,[0,4,7]) # inputs the appropriate tone degress for the chord type
        
    elif type_ == 1: # major triad add 9
        Type = "major triad add 9"
        tone_data = degrees(key,[0,2,4,7])
        
    elif type_ == 2: # sus4 ∆7
        Type = "sus4 ∆7"
        tone_data = degrees(key,[0,5,7,11])

    elif type_ == 3: # major 7
        Type = "major 7"
        tone_data = degrees(key,[0,4,7,11])
        
    elif type_ == 4: # dom7
        Type = "dom7"
        tone_data = degrees(key,[0,4,7,10])

    elif type_ == 5: # m7
        Type = "m7"
        tone_data = degrees(key,[0,3,7,10])

    elif type_ == 6: # minor triad
        Type = "minor triad"
        tone_data = degrees(key,[0,3,7])

    elif type_ == 7: # major 6
        Type = "major 6"
        tone_data = degrees(key,[0,4,7,8])

    elif type_ == 8: # ∆7#11
        Type = "∆7#11"
        tone_data = degrees(key,[0,6,7,11])

    elif type_ == 9: # m7#11
        Type = "m7#11"
        tone_data = degrees(key,[0,3,6,7,10])

    elif type_ == 10: # 7#11
        Type = "Mm7#11"
        tone_data = degrees(key,[0,4,6,7,10])
        
    elif type_ == 11: # ∆7 flat 9
        Type = "∆7 flat 9"
        tone_data = degrees(key,[0,2,4,7,11])

    elif type_ == 12: # dom7 flat 9
        Type = "Mm7 flat 9"
        tone_data = degrees(key,[0,1,4,7,10])

    elif type_ == 13: # m7 flat 9
        Type = "m7 flat 9"
        tone_data = degrees(key,[0,1,3,7,10])

    elif type_ == 14: # minor triad flat 9
        Type = "minor triad flat 9"
        tone_data = degrees(key,[0,1,3,7])

    elif type_ == 15: # sus4
        Type = "sus4"
        tone_data = degrees(key,[0,5,7])
    
    elif type_ == 16: # dim
        Type = "dim"
        tone_data = degrees(key,[0,3,5])

    elif type_ == 17: # half dim
        Type = "half dim7"
        tone_data = degrees(key,[0,3,6,10])

    elif type_ == 18: # fully diminished 
        Type = "fully diminished"
        tone_data = degrees(key,[0,6,9])

    elif type_ == 19: # open 5th
        Type = "open 5"
        tone_data = degrees(key,[0,7])

    elif type_ == 20: # open 4th
        Type = "open 4"
        tone_data = degrees(key,[0,5])

    elif type_ == 21: # open 3rd
        Type = "major 3rd"
        tone_data = degrees(key,[0,4])

    elif type_ == 22: # Aug
        Type = "Aug"
        tone_data = degrees(key,[0,4,8])

    elif type_ == 23: # Aug 7
        Type = "Aug7"
        tone_data = degrees(key,[4,8,10])
        
    elif type_ == 24: # Aug ∆7
        Type = "Aug ∆7"
        tone_data = degrees(key,[0,4,8,11])

    elif type_ == 25: # 7 flat 13
        Type = "7 flat 13"
        tone_data = degrees(key,[0,4,7,8,10])
    
    elif type_ == 26: # 7 #13
        Type = "7 #13"
        tone_data = degrees(key,[0,4,7,8,10])

    elif type_ == 27: # sus4 m7
        Type = "sus4 m7"
        tone_data = degrees(key,[0,5,7,10])

    elif type_ == 28: # open major 7
        Type = "open major 7"
        tone_data = degrees(key,[0,11])
    
    elif type_ == 29: #silence
        Type = "silence"
        key = 0
        tone_data = degrees(key,[0])
    
    elif type_ == 30: # single note w/base
        Type = "single note w/base"
        tone_data = degrees(key,[0])
    
    elif type_ == 31: # single note w/out base
        Type = "single note no base"
        tone_data = degrees(key,[0])
        key = 0

    elif type_ == 32: # open minor 7
        Type = "minor 7th"
        tone_data = degrees(key,[0,10])
    
    elif type_ == 33: # open 6th
        Type = "open 6th"
        tone_data = degrees(key,[0,9])

    elif type_ == 34: # diminish 6th
        Type = "dim 6th"
        tone_data = degrees(key,[0,8])
    
    freqs = tone_data[0]
    I = tone_data[1]
    inver = inversions(key)                     # adds in base potential chord inversions
    freqs = np.append(freqs,inver[0][:,0])
    I = np.append(I,inver[0][:,1])
    for i in range(0,len(I)):                           # adds in overtones and decay intensities 
        for j in range(0,10):
            c3 = np.random.rand()
            freqs = np.append(freqs, freqs[i]*(2+j)/2)
            I = np.append(I, I[i]*c3*np.exp(-.1*j))
    
    freqs = np.reshape(freqs,(len(freqs),1))
    I = np.reshape(I,(len(I),1))

    
    tone_data = np.append(freqs,I,1)   
    
    
    return  [tone_data,Type,inver[1],inver[2]]


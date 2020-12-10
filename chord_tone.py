from inversions import inversions
import numpy as np


# Each conditional represents different chord type.


def chord_tone(x,key):
    Type = []
    type_ = x
    I = []
    freqs = []

    if type_ == 0: # major triad
        Type = "major triad"
        for n in range(0,11): # nth octave
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key * k)                # This adds the frequencies for the octave
            freqs= np.append(freqs, (key + 4*2*key/12) * k)
            freqs= np.append(freqs, (key + 7*2*key/12) * k)
            
            L = len(freqs)/(n+1)                            # Generates intensities that peak in 
            L = int(L)                                      # middle octaves with randomn noise term
            for i in range(0,L):                
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )
                

    elif type_ == 1: # major triad add 9
        Type = "major triad add 9"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key * k)
            freqs= np.append(freqs, (key + 4*key*2/12) * k)
            freqs= np.append(freqs, (key + 7*2*key/12) * k)
            freqs= np.append(freqs, (key + 2*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )
    
    elif type_ == 2: # sus4 ∆7
        Type = "sus4 ∆7"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key + 7*2*key/12) * k)
            freqs= np.append(freqs, (key +5*2*key/12) * k)
            freqs= np.append(freqs, (key +11*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )

    elif type_ == 3: # major 7
        Type = "major 7"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +4*key*2/12) * k)
            freqs= np.append(freqs, (key +7*2*key/12) * k)
            freqs= np.append(freqs, (key+11*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )
        
    elif type_ == 4: # dom7
        Type = "dom7"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +4*key*2/12) * k)
            freqs= np.append(freqs, (key +7*2*key/12) * k)
            freqs= np.append(freqs, (key+10*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 5: # m7
        Type = "m7"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +3*key*2/12) * k)
            freqs= np.append(freqs, (key +7*2*key/12) * k)
            freqs= np.append(freqs, (key+10*2*key/12) * k)
    
            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 6: # minor triad
        Type = "minor triad"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +3*key*2/12) * k)
            freqs= np.append(freqs, (key +7*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 7: # major 6
        Type = "major 6"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +4*key*2/12) * k)
            freqs= np.append(freqs, (key +7*2*key/12) * k)
            freqs= np.append(freqs, (key+8*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 8: # ∆7#11
        Type = "∆7#11"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +4*key*2/12) * k)
            freqs= np.append(freqs, (key +7*2*key/12) * k)
            freqs= np.append(freqs, (key+11*2*key/12) * k)
            freqs= np.append(freqs, (key+ 6*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 9: # m7#11
        Type = "m7#11"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +3*key*2/12) * k)
            freqs= np.append(freqs, (key +7*2*key/12) * k)
            freqs= np.append(freqs, (key+10*2*key/12) * k)
            freqs= np.append(freqs, (key+ 6*2*key/12) * k)
            
            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 10: # 7#11
        Type = "Mm7#11"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +4*key*2/12) * k)
            freqs= np.append(freqs, (key +7*2*key/12) * k)
            freqs= np.append(freqs, (key+10*2*key/12) * k)
            freqs= np.append(freqs, (key+ 6*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 11: # ∆7 flat 9
        Type = "∆7 flat 9"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +4*key*2/12) * k)
            freqs= np.append(freqs, (key+ 7*2*key/12) * k)
            freqs= np.append(freqs, (key+ 11*2*key/12) * k)
            freqs= np.append(freqs, (key+ 2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 12: # dom7 flat 9
        Type = "Mm7 flat 9"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key+ 4*key*2/12) * k)
            freqs= np.append(freqs, (key+ 7*2*key/12) * k)
            freqs= np.append(freqs, (key+10*2*key/12) * k)
            freqs= np.append(freqs, (key+ 2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 13: # m7 flat 9
        Type = "m7 flat 9"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key+ 3*key*2/12) * k)
            freqs= np.append(freqs, (key+ 7*2*key/12) * k)
            freqs= np.append(freqs, (key+ 10*2*key/12) * k)
            freqs= np.append(freqs, (key+ 2*key/12) * k)    

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 14: # minor triad flat 9
        Type = "minor triad flat 9"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key+ 3*key*2/12) * k)
            freqs= np.append(freqs, (key+ 7*2*key/12) * k)
            freqs= np.append(freqs, (key+ 2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 15: # sus4
        Type = "sus4"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key + 7*2*key/12) * k)
            freqs= np.append(freqs, (key +5*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 16: # dim
        Type = "dim"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key +3*2*key/12) * k)
            freqs= np.append(freqs, (key +5*2*key/12) * k)
            
            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 17: # half dim
        Type = "half dim7"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key+ 3*key*2/12) * k)
            freqs= np.append(freqs, (key+ 6*2*key/12) * k)
            freqs= np.append(freqs, (key+ 10*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 18: # fully diminished 
        Type = "fully diminished"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key+ 3*key*2/12) * k)
            freqs= np.append(freqs, (key+ 6*2*key/12) * k)
            freqs= np.append(freqs, (key+ 9*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 19: # open 5th
        Type = "open 5"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key + 7*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 20: # open 4th
        Type = "open 4"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key + 5*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 21: # open 3rd
        Type = "major 3rd"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key + 4*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 22: # Aug
        Type = "Aug"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key + 4*2*key/12) * k)
            freqs= np.append(freqs, (key + 8*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 23: # Aug 7
        Type = "Aug7"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key + 4*2*key/12) * k)
            freqs= np.append(freqs, (key + 8*2*key/12) * k)
            freqs= np.append(freqs, (key + 10*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 24: # Aug ∆7
        Type = "Aug ∆7"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key + 4*2*key/12) * k)
            freqs= np.append(freqs, (key + 8*2*key/12) * k)
            freqs= np.append(freqs, (key + 11*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 25: # 7 flat 13
        Type = "7 flat 13"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key+ 4*key*2/12) * k)
            freqs= np.append(freqs, (key+ 7*2*key/12) * k)
            freqs= np.append(freqs, (key+ 10*2*key/12) * k)
            freqs= np.append(freqs, (key+ 8*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )


    elif type_ == 26: # 7 #13
        Type = "7 #13"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key+ 4*key*2/12) * k)
            freqs= np.append(freqs, (key+ 7*2*key/12) * k)
            freqs= np.append(freqs, (key+ 10*2*key/12) * k)
            freqs= np.append(freqs, (key+ 8*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )

    elif type_ == 27: # sus4 m7
        Type = "sus4 m7"
        for n in range(0,11):
            k = np.power(2,n) # nth octave pitch
            freqs= np.append(freqs, key* k)
            freqs= np.append(freqs, (key + 7*2*key/12) * k)
            freqs= np.append(freqs, (key +5*2*key/12) * k)
            freqs= np.append(freqs, (key +10*2*key/12) * k)

            L = len(freqs)/(n+1)
            L = int(L)
            for i in range(0,L):
                xx = np.random.rand() 
                t1 = abs(1 / (n-5.5))
                t2 = (1 / (1+np.exp(-xx))) / 3
                I = np.append(I,(t1+t2) / 2 )
    
    
    inver = inversions()                     # adds in base potential chord inversions
    freqs = np.append(freqs,inver[0][:,0])
    I = np.append(I,inver[0][:,1])
    
    for i in range(0,len(I)):                           # adds in overtones and decay intensities 
        for j in range(0,10):
            c3 = np.random.rand()
            freqs = np.append(freqs, freqs[i]*(2+j)/2)
            I = np.append(I, I[i]*c3*np.exp(-.1*j))
    
    
    I = np.reshape(I,(len(I),1))
    freqs = np.reshape( freqs, (len(freqs),1))
    tone_data = np.append(freqs,I,1)   
    
    
    return  [tone_data,Type,inver[1],inver[2]]


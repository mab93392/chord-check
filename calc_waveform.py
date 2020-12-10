import numpy as np 




def calc_waveform(data,n):
    f = data[:,0]                                                # extracts frequncies
    coe = data[:,1]                                              # extracts intensity
    sample_rate = 44100
    t = .005
    t_step = 1 / (sample_rate)
    time_max = 2*int(t / t_step)
    time = []
    pts = []
    final_freq = []
    y_axis = [] 
    pts = [] 


    for j in range(0,time_max+1):                                         # makes time incriment
        time = np.append(time,j) 
        time[j] = t_step * (j + (n-1)*time_max) 
        pts = []
        
        for i in range(0,len(f)):                                       # computes sin term with
            final_freq = np.append(final_freq, 2 * np.pi * f[i])        # frequency and and instensity 
            pts = np.append(pts,coe[i] * np.sin(final_freq[i]*time[j]))
        
        y_axis = np.append(y_axis, sum(pts))                            # adds weighted sin terms 
                                                                        # at a time incriment

        
    time = np.reshape(time, (len(time),1))
    y_axis = np.reshape(y_axis,(len(y_axis),1))
    wave = np.append(time,y_axis,1)


    return wave


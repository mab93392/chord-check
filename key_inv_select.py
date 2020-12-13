# function determines the key or inversion of the chord

def key_inv_select(acts):
    apx = max(acts) # extracts max activation

    if apx == acts[0]:
        out = "A"
    elif apx == acts[1]:
        out = "A#"
    elif apx == acts[2]: 
        out = "B"
    elif apx == acts[3]:
        out = "C"
    elif apx == acts[4]:
        out = "C#"
    elif apx == acts[5]:
        out = "D"
    elif apx == acts[6]:
        out = "D#"
    elif apx == acts[7]:
        out = "E"
    elif apx == acts[8]:
        out = "F"
    elif apx == acts[9]:
        out = "F#"
    elif apx == acts[10]:
        out = "G"
    else:
        out = "G#"
    
    return out
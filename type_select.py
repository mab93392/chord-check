# selects type of of chord

def type_select(acts):
    apx = max(acts) # extracts max value from activations

    if apx == acts[0]:
        out = " "
    elif apx == acts[1]:
        out = "add 9"
    elif apx == acts[2]:
        out = "sus4 ∆7"
    elif apx == acts[3]:
        out = "∆7"
    elif apx == acts[4]:
        out = "7"
    elif apx == acts[5]:
        out = "m7"
    elif apx == acts[6]:
        out = "m"
    elif apx == acts[7]:
        out = "6"
    elif apx == acts[8]:
        out = "∆7#11"
    elif apx == acts[9]:
        out = "m7#11"
    elif apx == acts[10]:
        out = "7#11"
    elif apx == acts[11]:
        out = "∆7 flat9"
    elif apx == acts[12]:
        out = "7 flat9"
    elif apx == acts[13]:
        out = "m7 flat9"
    elif apx == acts[14]:
        out = "m flat9"
    elif apx == acts[15]:
        out = "sus4"
    elif apx == acts[16]:
        out = "dim"
    elif apx == acts[17]:
        out = "half dim"
    elif apx == acts[18]:
        out = "fully dim"
    elif apx == acts[19]:
        out = "open 5th"
    elif apx == acts[20]:
        out = "open 4th"
    elif apx == acts[21]:
        out = "majord 3rd"
    elif apx == acts[22]:
        out = "+"
    elif apx == acts[23]:
        out = "+7"
    elif apx == acts[24]:
        out = "+∆7"
    elif apx == acts[25]:
        out = "7 flat 13"
    elif apx == acts[26]:
        out = "7 #13"
    elif apx == acts[27]:
        out = "sus4 m7"
    
    return out

# converts numerical key option to text output
def name(deg):
    if deg == 0: 
        key_name = "A"
    
    elif deg == 1:
        key_name = "A#"

    elif deg == 2:
        key_name = "B"

    elif deg == 3:
        key_name = "C"
    
    elif deg == 4:
        key_name = "C#"

    elif deg == 5:
        key_name = "D"

    elif deg == 6:
        key_name = "D#"
    
    elif deg == 7:
        key_name = "E"
    
    elif deg == 8:
        key_name = "F"
    
    elif deg == 9:
        key_name = "F#"
    
    elif deg == 10:
        key_name = "G"
    
    elif deg == 11:
        key_name = "G#"
        
    return    key_name


import mysql.connector 
import numpy as np 
from key_weight_setup import key_weight_setup




def key_weight():
    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor() # establishes cursor

    cur.execute("SELECT * FROM key_weight") # retrieves desired values
    v = np.array(cur.fetchall())[:,1:]

    
    return v


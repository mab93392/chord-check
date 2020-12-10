import mysql.connector 
import numpy as np 
from key_weight_setup import key_weight_setup




def key_weight():
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()

    cur.execute("SELECT * FROM key_weight")
    v = np.array(cur.fetchall())[:,1:]

    
    return v


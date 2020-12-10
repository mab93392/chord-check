from type_weight_setup import type_weight_setup
import mysql.connector 
import numpy as np 
from chord_db_drop import tab_drop

def type_weight():
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()

    cur.execute("SELECT * FROM type_weight")
    v = np.array(cur.fetchall())[:,1:]
    
    return v


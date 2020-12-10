import mysql.connector 
import numpy as np 
from inv_weight_setup import inv_weight_setup


def inv_weight():
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()

    cur.execute("SELECT * FROM inv_weight")
    v = np.array(cur.fetchall())[:,1:]
    
    return v




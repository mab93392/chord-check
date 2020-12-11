
import mysql.connector 
import numpy as np 


def type_weight():
# connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor() # establishes cursor

    cur.execute("SELECT * FROM type_weight") # retrieves row
    v = np.array(cur.fetchall())[:,1:]
    
    return v


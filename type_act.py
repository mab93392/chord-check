import mysql.connector 
import numpy as np 


def type_act(row):
    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor() # establishes cursor

    cur.execute("SELECT * FROM k_act WHERE act_num = %s" % row) # retrieves data
    v = cur.fetchall()
    
    return v


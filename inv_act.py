import mysql.connector 
import numpy as np 



def inv_act(row):
    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()

    # retrieves wanted row
    cur.execute("SELECT * FROM inv_act WHERE act_num = %s" % row)
    v = cur.fetchall()
    
    return v


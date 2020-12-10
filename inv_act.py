import mysql.connector 
import numpy as np 
from inv_act_setup import inv_act_setup
from chord_db_drop import tab_drop

def inv_act(row):
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()

    cur.execute("SELECT * FROM inv_act WHERE act_num = %s" % row)
    v = cur.fetchall()
    
    return v


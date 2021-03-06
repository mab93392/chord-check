import mysql.connector 
import numpy as np 
from key_act_setup import key_act_setup
from chord_db_drop import tab_drop

def key_act(row):
    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor() # establishes cursor

    # retrieves values
    cur.execute("SELECT * FROM key_act WHERE act_num = %s" % row) 
    v = cur.fetchall()
    
    return v


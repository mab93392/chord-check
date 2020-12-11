import mysql.connector 
import numpy as np 
from chord_db_drop import tab_drop

def key_act_setup():
    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()

    for i in range(0,11):
        if i == 0:
            # creates table and establishes first column
            cur.execute("CREATE TABLE key_act (act_num INT AUTO_INCREMENT PRIMARY KEY, C1 FLOAT NOT NULL DEFAULT 0)")
        else:
            # extends column name statement
            cur.execute("ALTER TABLE key_act ADD (C%s FLOAT NOT NULL DEFAULT 0)" % (i+1))
        # populates table w/0's
        s = "INSERT INTO key_act(C%s)" % (i+1)   
        v = "VALUES(0)"
        cur.execute(s+v)
        chord_db.commit()
 
    # populates table with 1's in apropriate locations
    for i in range(0,11):
        s = "UPDATE key_act SET C%s = 1     WHERE act_num = %s"
        cur.execute(s,(i+1,i+1))
        chord_db.commit()
    
# key_act_setup()


    





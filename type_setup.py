import mysql.connector 
import numpy as np 


def type_setup():
    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor() # establishes cursor

    for i in range(0,27):
        if i == 0:
            # creates table and first column
            cur.execute("CREATE TABLE k_act (act_num INT AUTO_INCREMENT PRIMARY KEY, C1 FLOAT NOT NULL DEFAULT 0)")
        else:
            # continues adding columns
            cur.execute("ALTER TABLE k_act ADD (C%s FLOAT NOT NULL DEFAULT 0)" % (i+1))
        # creates name and value statements
        s = "INSERT INTO k_act(C%s)" % (i+1)   
        v = "VALUES(0)"
        cur.execute(s+v)
        chord_db.commit()
        
        # populates table with 1's in apropiate locations
    for i in range(0,27):
        s = "UPDATE k_act SET C%s = 1     WHERE act_num = %s"
        cur.execute(s,(i+1,i+1))
        chord_db.commit()








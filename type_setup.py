import mysql.connector 
import numpy as np 
from chord_db_drop import tab_drop
from chord import Chord

def type_setup():
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()

    for i in range(0,27):
        if i == 0:
            cur.execute("CREATE TABLE k_act (act_num INT AUTO_INCREMENT PRIMARY KEY, C1 FLOAT NOT NULL DEFAULT 0)")
        else:
            cur.execute("ALTER TABLE k_act ADD (C%s FLOAT NOT NULL DEFAULT 0)" % (i+1))
        s = "INSERT INTO k_act(C%s)" % (i+1)   
        v = "VALUES(0)"
        cur.execute(s+v)
        chord_db.commit()

    for i in range(0,27):
        s = "UPDATE k_act SET C%s = 1     WHERE act_num = %s"
        cur.execute(s,(i+1,i+1))
        chord_db.commit()


# type_setup()
# tab_drop("k_act")





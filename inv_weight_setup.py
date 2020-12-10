import mysql.connector 
import numpy as np 
from chord_db_drop import tab_drop



def inv_weight_setup():
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()
    cur.execute("CREATE TABLE inv_weight (weight_num INT AUTO_INCREMENT PRIMARY KEY, C1 FLOAT NOT NULL DEFAULT 0)")
    c_name = "C1"
    for j in range(0,11):
        k = np.random.random(882)
        vs = "%s" % round(k[0],5)
        if j == 0:
            for i in range(1,882):
                c_name += ",C%s" % (i+1)
                vs += ",%s" % round(k[i],5)
                cur.execute("ALTER TABLE inv_weight ADD (C%s FLOAT NOT NULL DEFAULT 0)" % (i+1))
                chord_db.commit()
        
        
        else:
            for i in range(1,882):
                vs += ",%s" % round(k[i],5)
    
    
        cur.execute("INSERT INTO inv_weight (" + c_name + ") VALUES(" + vs + ")" )
    chord_db.commit()
    



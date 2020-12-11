import mysql.connector 
import numpy as np 
from chord_db_drop import tab_drop

def key_weight_setup():
    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()
    # creates table and establishes first column
    cur.execute("CREATE TABLE key_weight (weight_num INT AUTO_INCREMENT PRIMARY KEY, C1 FLOAT NOT NULL DEFAULT 0)")
    # begins name statement
    c_name = "C1"
    for j in range(0,11):
        k = np.random.random(882)
        vs = "%s" % round(k[0],5) # begins value statement
        if j == 0:
            for i in range(1,882):
                # continues making name and value statements
                c_name += ",C%s" % (i+1)
                vs += ",%s" % round(k[i],5)
                cur.execute("ALTER TABLE key_weight ADD (C%s FLOAT NOT NULL DEFAULT 0)" % (i+1))
                chord_db.commit()
        
        
        else:
            for i in range(1,882):
                vs += ",%s" % round(k[i],5)
    
    # commits name and value statements
        cur.execute("INSERT INTO key_weight (" + c_name + ") VALUES(" + vs + ")" )
        chord_db.commit()
    
    
    

# key_weight_setup()
# tab_drop("key_weight")

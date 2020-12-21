import mysql.connector 
import numpy as np 


def type_weight_setup():
    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor() # establishes cursor

    # creates table and first column
    cur.execute("CREATE TABLE type_weight (weight_num INT AUTO_INCREMENT PRIMARY KEY, C1 FLOAT NOT NULL DEFAULT 0)")
    c_name = "C1" # begins making name statment
    for j in range(0,27):
        k = np.random.random(882)
        vs = "%s" % round(k[0],5) # begins making value statement
        if j == 0:
            # makes first row of table
            for i in range(1,882):
                c_name += ",C%s" % (i+1) # continues name statement
                vs += ",%s" % round(k[i],5) # continue value statement
                cur.execute("ALTER TABLE type_weight ADD (C%s FLOAT NOT NULL DEFAULT 0)" % (i+1))
                chord_db.commit() 
        
        
        else: # makes other 21 rows of table
            for i in range(1,882): 
                vs += ",%s" % round(k[i],5)
    
    
        cur.execute("INSERT INTO type_weight (" + c_name + ") VALUES(" + vs + ")" )
        chord_db.commit()
    
    


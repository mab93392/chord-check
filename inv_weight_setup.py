import mysql.connector 
import numpy as np 




def inv_weight_setup():

    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()
    # creates table
    cur.execute("CREATE TABLE inv_weight (weight_num INT AUTO_INCREMENT PRIMARY KEY, C1 FLOAT NOT NULL DEFAULT 0)")
    # begins making name portion of commit statement
    c_name = "C1"
    for j in range(0,11):
        # begins making weight values
        k = np.random.random(882)
        vs = "%s" % round(k[0],5)
        if j == 0:
            # continues making value and name statements
            for i in range(1,882):
                c_name += ",C%s" % (i+1)
                vs += ",%s" % round(k[i],5)
                cur.execute("ALTER TABLE inv_weight ADD (C%s FLOAT NOT NULL DEFAULT 0)" % (i+1))
                chord_db.commit()
        
        else:
            for i in range(1,882):
                vs += ",%s" % round(k[i],5)
    
        # executes created statements
        cur.execute("INSERT INTO inv_weight (" + c_name + ") VALUES(" + vs + ")" ) 
    chord_db.commit()
    



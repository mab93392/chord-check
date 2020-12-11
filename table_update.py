import mysql.connector 
import numpy as np 
from key_weight import key_weight

def table_update(data,tb_name):
        # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()  # establishes cursor

    shape = np.shape(data) # extracts shape of data

    depth = shape[0]
    length = shape[1]

    upd_list = [] # initializes array of update value statements
    for j in range(0,depth): # creates a list of column update value statements for each row
        for i in range(0,length): # creates the actual colum update value statement for jth row
            if i == 0:
                s = "C1 = %s" % data[j][i]
            else:
                s += ", C%s = %s" % ((i+1),data[j][i])
        upd_list = np.append(upd_list,s) # list of update value statements
    
        cur.execute("UPDATE " + tb_name + " SET " + upd_list[j] + " WHERE weight_num = %s" % (j+1))
        chord_db.commit()
    





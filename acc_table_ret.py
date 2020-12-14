import mysql.connector 
import numpy as np 
from chord_db_drop import tab_drop

def acc_table_ret(col_name):

    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor() # establishes cursor

    # retrieves column data
    cur.execute("SELECT "+ col_name + "FROM accuracy")
    out = cur.fetchall()

    return out

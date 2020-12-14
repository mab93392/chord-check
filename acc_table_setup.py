import mysql.connector 
import numpy as np 
from chord_db_drop import tab_drop

def acc_table_setup():

    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor() # establishes cursor

    # creates "create table statement"
    stmt1 = "CREATE TABLE accuracy " # creates table 
    stmt2 = "(test_num INT AUTO_INCREMENT PRIMARY KEY, " # makes 1st column
    stmt3 = "av_er FLOAT NOT NULL DEFAULT 0, " # makes 2nd column
    stmt4 = "total_acc FLOAT NOT NULL DEFAULT 0, " # makes 3rd column
    stmt5 = "key_acc FLOAT NOT NULL DEFAULT 0, " # makes 4th column 
    stmt6 = "inv_acc FLOAT NOT NULL DEFAULT 0, " # makes 5th column
    stmt7 = "type_acc FLOAT NOT NULL DEFAULT 0)" # makes 6th colmn

    cur.execute(stmt1+stmt2+stmt3+stmt4+stmt5+stmt6+stmt7) # actually executes creation stamtent

import mysql.connector 

def acc_write(data,col_n):

    # connects to database
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor() # establishes cursor

    cur.execute("INSERT INTO accuracy( " + col_n + ") VALUES( " + str(data) + ")" ) # inserts data
    chord_db.commit()

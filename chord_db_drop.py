import mysql.connector 

def tab_drop(x):
    chord_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "fm2a85xm",
        database = "chord_data"
    )

    cur = chord_db.cursor()

    cur.execute("DROP TABLE %s" % x)

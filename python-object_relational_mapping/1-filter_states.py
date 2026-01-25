#!/usr/bin/python3
"""first ORM"""

import MySQLdb
import sys




def connection():
    usrnm = sys.argv[1]
    psswrd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
         host='localhost',
         port=3306,
         user=usrnm,
         password=psswrd,
         database=db_name)

    cursor = db.cursor()

    sql = (
        "SELECT * FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY states.id ASC;")

    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    connection()

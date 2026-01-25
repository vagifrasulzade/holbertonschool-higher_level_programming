#!/usr/bin/python3
"""This script lists all states with a name"""
import MySQLdb
import sys


def connection():
    usrnm = sys.argv[1]
    psswrd = sys.argv[2]
    db_name = sys.argv[3]
    stn = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=usrnm,
        password=psswrd,
        database=db_name)

    cursor = db.cursor()

    sql = ("SELECT * FROM states "
           "WHERE name=%s ORDER BY "
           "states.id ASC;".format(str(stn)))

    cursor.execute(sql, (stn,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    connection()

#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""

import sys
import pymysql
pymysql.install_as_MySQLdb()  # Windows-da MySQLdb əvəzinə PyMySQL istifadə
import MySQLdb


def connection():
    """Connects to the database and prints all states sorted by id."""
    usrnm = sys.argv[1]
    psswrd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usrnm,
        passwd=psswrd,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    connection()
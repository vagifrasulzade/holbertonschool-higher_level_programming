#!/usr/bin/python3
"""This script lists all cities of a given state from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def connection():
    usrnm = sys.argv[1]
    psswrd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=usrnm,
        password=psswrd,
        database=db_name)

    cursor = db.cursor()

    sql = ("SELECT cities.name "
           "FROM cities "
           "JOIN states ON cities.state_id = states.id "
           "WHERE states.name = %s "
           "ORDER BY cities.id ASC;")

    cursor.execute(sql, (state_name, ))

    rows = cursor.fetchall()

    cities = []
    for row in rows:
        cities.append(row[0])

    print(", ".join(cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    connection()

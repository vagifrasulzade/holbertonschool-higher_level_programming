#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.

"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
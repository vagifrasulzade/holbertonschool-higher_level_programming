#!/usr/bin/python3
"""first ORM"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3], port=3306
        )

    cs = db.cursor()
    cs.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cs.fetchall()
    for row in rows:
        print(row)

    cs.close()
    db.close()

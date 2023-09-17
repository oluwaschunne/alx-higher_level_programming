#!/usr/bin/python3
"""this lists all the states in the given database"""
import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states  WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()

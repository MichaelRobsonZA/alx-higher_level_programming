#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
This version is safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (search_name,))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()

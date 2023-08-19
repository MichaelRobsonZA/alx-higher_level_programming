#!/usr/bin/python3
"""Lists all values in the states table of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    search_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (search_name,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()

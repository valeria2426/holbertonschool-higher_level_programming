#!/usr/bin/python3
import MYSQLdb
import sys

if __name__ == '__main__':
    db = MYSQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY Id ASC")
    for row in cursor.fetchall():
        print(row)
    db.close()
    cursor.close()

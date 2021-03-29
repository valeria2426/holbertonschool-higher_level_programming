#!/usr/bin/python3
"""
list all states, by id username. password, and database names.
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    data_base = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         database=argv[3],
                         host='localhost',
                         port=3306
                         )
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close
    data_base.close

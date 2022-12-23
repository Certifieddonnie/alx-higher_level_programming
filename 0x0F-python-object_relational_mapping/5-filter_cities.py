#!/usr/bin/python3
"""
A Script that takes in the name of a state as an
argument and lists all cities of that state, using
the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Connects to the databases and retrieves list
    of all cities.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )

    db_cur = db_connect.cursor()

    db_cur.execute("SELECT cities.id, cities.name\
        FROM cities JOIN states ON cities.state_id\
            = states.id WHERE states.name = %s\
                ORDER BY cities.id", (argv[4], ))

    lst = db_cur.fetchall()
    print(", ".join([item[1] for item in lst]))

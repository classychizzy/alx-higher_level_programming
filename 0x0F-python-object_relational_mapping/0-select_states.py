#!/usr/bin/python3


"""a script that shows all states in the database
hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    """connection to the database"""
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
        )

    """create an instance of 'cursor' class
    which is used to execute SQL statements
    in python """
    cursor = mydb.cursor()
    """ to show all columns in the database"""
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')
    """command to fetch all rows"""
    results = cursor.fetchall()
    for result in results:
        print(result)

    mydb.close()

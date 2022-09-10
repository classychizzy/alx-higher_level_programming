#!/usr/bin/python3


"""a script that shows all states in the database
hbtn_0e_0_usa"""

import MySQLdb


"""connection to the database"""
mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="classychizzy",
        password="@Chizzy2636",
        db="hbtn_0e_0_usa"
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

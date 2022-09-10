#!/usr/bin/python3
"""a script that lists all state names starting
with upper N"""


import MySQLdb

mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="classychizzy",
        passwd="@Chizzy2636",
        db="hbtn_0e_0_usa"
        )

"""get cursor object"""
cursor = mydb.cursor()

"""execute the query"""
cmd = """SELECT id, name
        FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER by id ASC;"""
cursor.execute(cmd)
"""fetch all rows"""
results = cursor.fetchall()

"""loop through result"""
for result in results:
    print(result)

cursor.close()
mydb.close()

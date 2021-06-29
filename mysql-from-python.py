import os
import datetime
import pymysql

# connect to the database
connection = pymysql.connect(host='localhost',
password='',
db='Chinook')

try:
    # run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
        Friends(name char(20), age int, DOB datetime);""")
        for row in cursor:
            print(row)
finally:
    # close the connection to sql
    connection.close()
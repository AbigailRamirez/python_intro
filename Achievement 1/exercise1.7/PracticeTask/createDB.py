import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE my_database")

cursor.execute("USE my_database")

conn.commit()

conn.close()
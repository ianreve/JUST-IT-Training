import mysql.connector

conn = mysql.connector.connect(host = "localhost", database ="leisure_centre", user = "root", password = "Watford2017" )

cursor = conn.cursor()
cursor.execute("SELECT * FROM Course;")
for database in cursor:
    print(database)
cursor.close()
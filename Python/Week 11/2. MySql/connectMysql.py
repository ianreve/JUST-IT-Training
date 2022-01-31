import mysql.connector

# conn = mysql.connector.connect(host = "localhost", database ="leisure_centre", user = "root", password = "Watford2017" )

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM Course;")
# for database in cursor:
#     print(database)
# cursor.close()

conn = mysql.connector.connect(host = "localhost", database ="c5Music", user = "root", password = "pasword123" )

if conn.is_connected():
    print("connected to DB")
else:
    print("Not connected to DB")

cursor = conn.cursor(prepared=True)
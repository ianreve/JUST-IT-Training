from sqlite3 import Row
from connectDB import * 
def readSongs():
    cursor.execute("SELECT * FROM songs")
    row = cursor.fetchall()
    for record in row:
        print(record)
# readSongs()
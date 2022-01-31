from matplotlib.pyplot import connect
from connectDB import * 
import time


def deleteSongs():
    idField = int(input("Enter the Id of the record you want to delete: "))

    try:
        cursor.execute(f"DELETE FROM songs WHERE SongID = {idField}")
        conn.commit()
        print(f"Record {idField} Deleted")
        time.sleep(3)
        cursor.execute('SELECT * FROM songs')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
           print(f"Song {idField} not updated")
    
    finally:
           conn.close()

# deleteSongs()
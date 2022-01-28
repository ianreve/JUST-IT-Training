from connectDB import * 
import time

def seachSongs():
    fieldName = input("Which field would you like to search (Title, Artist, Genre): ")
    searchValue = input("Enter the search value for the field: ")
    print(f"User search Value {searchValue}")
    searchValue = "'" + searchValue + "'" 
    print(f"User search input {searchValue}")

    try:
        cursor.execute(f"SELECT * FROM songs WHERE {fieldName} = {searchValue}")
        conn.commit()
    
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print(f"Song {searchValue} Not found")
    finally:
        conn.close()
seachSongs()


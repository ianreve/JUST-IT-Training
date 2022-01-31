from numpy import rec
from connectMysql import *

import time
def addMember():
    members = []

    fname = input("Enter Firstname : ")
    lname = input("Enter Lastname : ")
    email = input("Enter Email : ")

    members.append(fname)
    members.append(lname)
    members.append(email)

    try:
        cursor.excute("INSERT INTO members VALUES(NULL, %s, %s, %s", members)
        conn.commit()
        print(f"Added member {fname}")

        time.sleep(3)
        cursor.excute("SELECT * FROM members")
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        raise("Record not added")
    finally:
        conn.close()
addMember()

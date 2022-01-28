import sqlite3 # import sqlite3 library

conn = sqlite3.connect("Week 10/Part 11. DB Operations/1. SQlite/c5Music.db") # create and connect the db
cursor = conn.cursor() # cursor method iterate our db

from connectMysql import *


"create database"
cursor.execute("CREATE DATABASE c5Music;")

#show databases in localhost
cursor.execute("SHOW DATABASES;")
for databases in cursor:
    print(databases)
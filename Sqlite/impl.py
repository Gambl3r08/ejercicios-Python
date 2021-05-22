from os import curdir
import dbmanager
import sqlite3
DB = dbmanager.createDB("datos")
cursor  = DB.cursor()
datos = cursor.fetchall()

for i in datos:
    print(i[0], " ", i[1])



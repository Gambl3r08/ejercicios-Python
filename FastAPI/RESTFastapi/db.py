from os import error
from sqlite3.dbapi2 import Cursor
from pydantic import BaseModel
import sqlite3
from sqlite3 import Error


class User(BaseModel):
    name: str
    password: str
    email: str

def InitDB():
    try:
       con = sqlite3.connect('userdb.db')
       #cursor = con.cursor()
       #cursor.execute("CREATE TABLE users (id integer PRIMARY KEY, name text, password text, email text)")
       #con.commit()
       return con
       print("Connection is established: Database is created in memory")
    except Error:
        print(Error)


con = InitDB()





def SaveUser(user: User, con):
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO users VALUES ( '{}', '{}', '{}' )".format(user.name, user.password, user.email))
        return "message: OK"
    except Error:
        return {"Error":Error}

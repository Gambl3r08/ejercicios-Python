import sqlite3

def createDB(name: str):
    try:
        db = sqlite3.connect(name)
        return db
    except:
        print("error al crear la base de datos: ", name)

def createCursor(db: sqlite3):
    try:
        cursor = db.cursor()
        return cursor
    except:
        print("Error al crear cursor")

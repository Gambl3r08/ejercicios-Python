from fastapi import FastAPI
from db import User, SaveUser, InitDB

app = FastAPI()

@app.post('/createuser')
async def createuser(user: User):
    con = InitDB()
    err = SaveUser(user, con)    
    return err

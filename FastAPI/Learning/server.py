from fastapi import FastAPI
from typing import Optional
from fastapi.params import Query
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
async def home():
    return {"Message": "OK"}

# Path parameters
@app.get('/items/{item_id}')
async def getItem(item_id: int):
    return {"item_id": item_id}

# Query parameters
@app.get('/query')
async def query(skip: int = 0, limit : int = 10):
    return{"Datos: ":[skip, skip+limit]}


# Defaults and Optionals
# http://localhost:8000/default/222s?q=2
@app.get('/default/{item_id}')
async def default(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return{"item_id": item_id}


#Multiple path and query parameters
@app.get('/mul/{mul1}/item/{mul2}')
async def multiples(mul1, mul2):
    items = {"mul1": mul1, "mul2": mul2}
    return items

#Required query parameters

@app.get('/req/{item_req}')
async def read_req(item_req: str, needy: str):
    item = {"item": item_req, "needy": needy}
    return item

# Request body

class item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get('/reqbody')
async def reqbody(item: item):
    return item

@app.post('/reqbodypost')
async def reqpost(item: item):
    return item


# Query Parameters and String Validations

@app.get('/validar/')
async def validar(q: Optional[str] = Query(None, max_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


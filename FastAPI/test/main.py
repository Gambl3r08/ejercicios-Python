from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    name: str;
    price: float;
    is_offer: Optional[bool] = None;

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get('/')
def index():
    return{"hello":"world"}


@app.get('/datos')
async def getDatos(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price}
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import datetime

# Let's create the app
app = FastAPI()

# Create a demo db
demo_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None

class AnotherItem(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.6
    tags: list[str] = []

# Create a small database
items = {
    '1': {
        'name': 'A',
        'price': 50.2
    },
    '2': {
        'name': 'B',
        'description': 'This is B',
        'price': 62,
        'tax': 10
    },
    '3': {
        'name': 'C',
        'description': None,
        'price': 50.2,
        'tax': 10.6,
        'tags': []
    }
}

# We might have datatype that might not compatible to database
@app.put('/items/{id}')
async def update_item(id: str, item: Item):
    json_compatble_item = jsonable_encoder(item)
    demo_db[id] = json_compatble_item
    return 'Success'

# Let's create a route
@app.get('/another_items/{item_id}', response_model=AnotherItem)
async def read_item(item_id: str):
    return items.get(item_id)

@app.put('/diff_item/{item_id}')
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded
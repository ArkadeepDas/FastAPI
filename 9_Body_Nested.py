from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl

# Let's create the app
app = FastAPI()

# Let's create a body
class Image(BaseModel):
    # It will take URL
    url: HttpUrl
    name: str

# Let's create a Body
class Item(BaseModel):
    # Here tags is list off items. We can specify what kind of list it would be
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    # Here list will take only strings
    # If we change it to 'int' then we can see some error if we pass string
    tags : list[str] = []
    # In place of list we can use set, whic will return 
    # Now let's see the Nested Boy
    #############################################################################
    # The nesting model comes in the '/docs'
    image: Image | None = None

# Route
@app.put('/item/{item_id}')
async def update_item(item_id: int, item:Item):
    results = {'item_id': item_id, 'item': item}
    return results
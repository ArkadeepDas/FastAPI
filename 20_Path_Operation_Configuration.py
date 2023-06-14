from fastapi import FastAPI, status
from pydantic import BaseModel
from enum import Enum

# Let's create the app
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

# After adding the tag it is much more organized
# We can see in /docs there are two types of routes

# We can do this using Enum
# We can add multiple tags
class Tags(Enum):
    items = 'items'
    users = 'users'

# Let's create the route
# We can add summary in decorator
@app.post('/items/', response_model = Item, status_code = status.HTTP_201_CREATED, tags = [Tags.items])
async def create_item(item: Item):
    # This comment bellow will show in the route /docs
    '''
    Create a item with information:
    - **name**: Name should be there
    - **description**: You can put some description there
    - **price**: Assign the price
    - **tax**: If item don't have tax then you can ignore
    - **tag**: Set unique tag for items
    '''
    return item

@app.get('/items/', tags = [Tags.items])
async def read_items():
    return [{'name': 'Car', 'price': 10}]

@app.get('/users/', tags = [Tags.users])
async def read_user():
    return [{'user_name': 'Arka'}]

# If we don't want to use any valid end point then we can use depricated
# It is still there. We can use it but not in real use
@app.get('/elements/', tags = ['Notinuse'], deprecated = True)
async def read_element():
    return [{'item_id': 1}]
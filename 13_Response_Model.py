from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
from typing import Literal

# Let's create the app
app = FastAPI()


# Let's create a body
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

# Route
@app.post('/items')
async def create_item(item: Item):
    return {'Item': item}

# Here we are returning a plain text password
class UserIn(BaseModel):
    username: str
    emal: EmailStr
    full_name: str | None = None

# Let's create a class and inherit from UserIn
class UserBase(UserIn):
    password: str


# Route
# Now because of response_model our schema in /docs knows what to do
@app.post('/user', response_model = UserBase)
async def create_user(user: UserIn):
    return {'User': user}

# Let's see some response model exluding 
items = {
    'A': {'name': 'A', 'price': 50.2},
    'B': {'name': 'B', 'description': 'This is B', 'price': 60, 'tax': 9},
    'C': {'name': 'C', 'price': 80, 'tax': 8}
}

# Route
@app.get('/items/{item_id}', response_model=Item, response_model_exclude_unset=True)
# Now it will take values between these three valus
# The bellow line says it has to be 
async def read_item(item_id: Literal['A', 'B', 'C']):
    return items[item_id]

#######################################################################################################
# For 'A' we don't set 'tax'. It has default value but here we use 'response_model_exclude_unset=True'
# So which is not present will not shown.
# Same thing for 'B'
# If we pass the default value it also worked. 'C' is the example for that.
#######################################################################################################

# There is response_mode_include, response_model_exclude. It will include or exclude certain values.
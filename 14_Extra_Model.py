from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Literal, Union

# Let's create the app
app = FastAPI()

# Let's create a body
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UsrDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None

def fake_password_hasher(raw_pass: str):
    return f'super_secret{raw_pass}'

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    # Just pass the dictionary and add the value in 'hashed_password'
    # Now it's olny going to pull in the fields that we need
    # Here we are providing password. But it does not accept it.
    user_in_db = UsrDB(**user_in.dict(), hashed_password=hashed_password)
    print(user_in_db)
    print('UserIn dict: ', user_in.dict())
    print('User saved')
    return user_in_db

# Route
# Fix the response model
# We don't want any password to return
@app.post('/User', response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

# Now let's see union 
class BaseItem(BaseModel):
    description: str
    typ: str

# Inherit from BaseItem
class CarItem(BaseItem):
    typ = 'Car'

# Inherit from BaseItem
class PlaneItem(BaseItem):
    typ = 'Plane'
    size: int

# Let's setup a small dictionary item
items = {
    'item_1': {'description': "Tathagata's Car", 'typ': 'Car'},
    'item_2': {'description': "Souvik's Plane", 'typ': 'Plane', 'size': 5}
}

# Route
# Fix the response model by combining both body
# Order of Union matters
@app.get('/items/{item_id}', response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: Literal['item_1', 'item_2']):
    return items[item_id]

# We can fix the type
@app.get('/items_id', response_model=dict[str, str])
async def data():
    return {'Name': 'Arka', 'Roll': 10}


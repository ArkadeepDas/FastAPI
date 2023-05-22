from enum import Enum
from fastapi import FastAPI

app = FastAPI()
# No path given
@app.get('/', description='This is our first project on FastAPI')
async def root():
    return {'message' : 'Hello World'}

# Path Parameters help us to set path for different different purpose
# It's standard get request
# GET request is used to retrieve data from a specified resource    
# It should not be used for action that modify data
@app.get('/demo')
async def new_path():
    return {'message' : "It's in /demo path"}

# Add anothe path
@app.get('/demo/{id}')
# We can say our id type. Here we set int
# If we pass string then there will be a error
# Basically we can fix the parameter type
async def get_id(id : int):
    return {'ID: ' : id}

@app.get('/users/{user_id}')
# Here we fix the parameter value to string
async def users(user_id : str):
    return {'User Id: ': user_id}

# Let's create another route with same path
@app.get('/users/me')
async def current_user():
    return {'Message: ' : 'This is from current user' }

#################################################################
#################################################################
# Now in this situation when we pass path parameter 'users/me', 
# '/users/{user_id}' hits and message shown {'User Id': 'me'}
# FastAPI find the first matching route
# The order that puting these routes matters

# Let's start with Enum
class food_structure(Enum):
    fruits = "Fruits"
    vegetables = "Vegetables"
    meat = "Meat"

@app.get('/food/{food_name}')
async def get_foodname(food_name = food_structure):
    if food_name == 'Meat':
        return {'Message: ': 'Non-veg'}
    if food_name == 'Vegitables':
        return {'Message: ': 'Veg'}
    else:
        return {'Message: ': 'Some Fruits'}
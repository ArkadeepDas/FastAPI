from fastapi import FastAPI
from pydantic import BaseModel

# Let's create the app first
app = FastAPI()

# We need to create a class
class Item(BaseModel):
    # We can think of it as a dictionary
    # We make description and tax optional
    name:str
    description:str | None = None
    price:float
    tax:float | None = None

# Here we ae going to use POST request
# POST request is commonly used when you want to submit data to a server for further processing.
# When the data is going to be saved for the first time
@app.post('/items')
# Here we use pydantic BaseModel extension
#########################################################
# Here 'Item' is request body
######################################################### 
async def create_item(item:Item):
    # Because the function return 'item', we have to figure out how to pass this information
    # We don't use path parameters here
    # We use pydantic
    return item

#########################################################
# Now it will work in '/docs'
#########################################################

# Let's do something with actual items
@app.post('/new_items')
async def create_new_item(item:Item):
    # It is a predefine method in pydantic
    # It converts BaseModel to dictionary
    item_dic = item.dict()
    # Because tax is a attribute of a class, but not dictionary
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dic.update({'price with tax':price_with_tax})
    return item_dic
# In FastAPI, by default, the output of a POST,PUT request is not shown in the URL.

# The PUT request is used to update or replace an existing resource with new data
@app.put('/new_items/{item_id}')
async def create_item_with_put(item:Item, item_id:int, qp:str|None = None):
    result = {'item_id' : item_id, **item.dict()}
    if qp:
        result.update({'qp' : qp})
    return result
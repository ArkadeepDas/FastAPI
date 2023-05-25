from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
# Let's create the app
app = FastAPI()

##################################################################
# There is another way we can set multiple examples
# In Body() there is a option 'examples', where we can set multiple examples
# It will show as a drop down list

# Create example using 3 ways
class Item(BaseModel):
    # 2) Use Filed() and set example
    name: str | None = Field(None, example='Car')
    description: str | None = Field(None, example='SUV')
    price: float = Field(..., example=16.5)
    tax: float | None = Field(..., example=1.67)
    # 1) We create this inside this body
    # class Config:
    #     schema_extra = {
    #         'example': {
    #             'name': 'Car',
    #             'description': 'SUV',
    #             'price': 16.5,
    #             'tax': 1.67
    #         }
    #     }

# Route
@app.put('/items/{item_id}')
# It takes Item and print the schema_extra. It takes example data
# Using Field and example as a parameter we can do the same thing
# 3) Same way we can add Body() in parameter. It will work same way
async def update_item(
    item_id: int,
    item: Item = Body(example={
        'name': 'Car',
        'description': 'SUV',
        'price': 16.5,
        'tax': 1.67
    })):
    results = {'item_id': item_id, 'item': item}
    return results
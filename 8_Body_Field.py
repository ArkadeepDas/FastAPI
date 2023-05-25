from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
# Let's create the app
app = FastAPI()

# Basic Body
class Item(BaseModel):
    name: str
    # Here we import Field from pydantic. Kind of same as Body, Path, Query.
    # Use in body
    description: str | None = Field(None, title = 'Description of the item', max_length = 300)
    price: float = Field(..., gt = 0, description = 'The price must be grater than zero')
    tax: float | None

# Route
@app.put('/items/{item_id}')
# Here we add embed=True
# We can see the change in /docs link
# If we add embed=True then there is a key, value pair else not
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {'item_id': item_id, 'item': item}
    return results
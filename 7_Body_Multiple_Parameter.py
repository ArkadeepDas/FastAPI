from fastapi import FastAPI
from fastapi import Path
from fastapi import Body
from pydantic import BaseModel

# Let's create the app
app = FastAPI()

# Let's create body
class Item(BaseModel):
    name: str
    description: str | None = None
    prise: float
    tax: float | None = None

# Let's create another body
class User(BaseModel):
    username: str
    full_name: str | None = None

class Importance(BaseModel):
    importnce: int

@app.put('/items/{item_id}')
# Here in the parameter we pass two body
# Remember non default parameter can't follow default parameter
# Just like Path and Query we can use Body object
async def update_item(*, item_id: int = Path(...,
                                          title='Id of item',
                                          ge=0,
                                          le=150),
                      q: str | None = None,
                      item: Item | None = None,
                      user: User | None = None,
                      importance: int = Body(...)):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if item:
        results.update({'item': item})
    if user:
        results.update({'user': user})
    return results
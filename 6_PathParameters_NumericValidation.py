from fastapi import FastAPI
from fastapi import Query
from fastapi import Path
# Let's create the app
app = FastAPI()

# It similar way of query parameter
# Here we are doing this with Path object
# Order of the parameters doesn't even matter
@app.get('/items_validation/{item_id}')
# ge = grater than equal, gt = grater than, le less than equal, lt = less than
async def read_items_validation(item_id:int = Path(..., title='Id of the item', ge=5), q:str|None = Query(None, alias='items_query')):
    results = {'item_id':item_id}
    if q:
        results.update({'q':q})
    return results
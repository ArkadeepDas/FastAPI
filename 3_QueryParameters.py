# Query Parameter is '?parameter' in the URL
from fastapi import FastAPI

app = FastAPI()

# Let's create a items Database
database = ['Arka', 'Tathagata', 'Souvik', 'Debapriya']

#############################################################
# It's work like a list truncation
# Let's initialize a query parameter
@app.get('/items')
# We are setting the limit here
# Because here limit is 5 it will show everything
# In the URL bar if we set '?start=2', it will show ['Souvik', 'Debapriya']
# In the URL bar if we set '?limit=2', it will show ['Arka', 'Tathagata']
async def get_items(start: int = 0, limit: int = 5):
    return database[start:limit]

# Let's make some query optional
@app.get('/items/{item_id}')
# 'item_id' must be string
##### 'q' is optional query. Type of 'q' is string #####
async def get_item(item_id: str, q: str | None = None):
    # If q have some value then it will work
    if q:
        return {'item_id: ': item_id, 'query: ': q}
    else:
        return {'item_id': item_id}

#############################################################
# If we pass '/items/Arka?q=ABCD' in our URL, it will show
# '{"item_id: ":"Arka","query: ":"ABCD"}' as output
#############################################################

# Let's see the type conversion 
@app.get('/gg/{item_id}')
# 'item_id' must be string
# 'q' is optional query. Type of 'q' is string
# For more than one parameter we use '&'
# Here when we use 'short' then we have to use '&'
async def get_itm(item_id: str, q: str | None = None, short: bool = False):
    # We can't have non-default parameters after default parameters
    item = {'item_id: ' : item_id}
    if q:
        # If there is a query then it will update
        item.update({'q:' : q})
    if not short:
        item.update({'Description' : 'This is demo query parameter'})
    return item

###################################################################
## Now if we run this with URL: 'http://127.0.0.1:8000/gg/Arka?q=ABCD&short=0' it will work
###################################################################
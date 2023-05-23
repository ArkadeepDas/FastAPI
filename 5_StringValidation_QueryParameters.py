from fastapi import FastAPI
from fastapi import Query

# Let's create the app first
app = FastAPI()

###########################################################
# We can have same path for different request(GET, POST, PUT etc.)
###########################################################

# Now we want to add some validation in query parameter
# Query parameter maxmimum 10 character
# So here we use Query()
# We can add many parameters, min_length, max_length, regex
# Here the default query is 'FixedQuery' and we remove the None, but we can set any value

############################################################
######################## :Output: ##########################
# "{"item id":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"FixedQuery"}"
@app.get('/items')
async def read_item(q:str = Query('FixedQuery', min_length = 3, max_length = 10)):
    result = {'item id' : [{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q:
        result.update({'q': q})
    return result

# Without having a default parameter we want required parameter
# '...' means we don't have default value but it has to something 
@app.get('/new_items')
async def read_item(q:str = Query(..., min_length = 3, max_length = 10)):
    result = {'item id' : [{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q:
        result.update({'q': q})
    return result
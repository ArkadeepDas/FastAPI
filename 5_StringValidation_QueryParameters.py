from fastapi import FastAPI
from fastapi import Query

# Let's create the app first
app = FastAPI()

###########################################################
# We can have same path for different request(GET, POST, PUT etc.)
###########################################################

# Now we want to add some validation in query parameter
# Query parameter maxmimum 10 character, minimum 3 character
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

# Let's see how we can add multiple options in single parameter
# Now it will take multiple input
@app.get('/list_items')
# Here it's('q') a optional parameter
# Now if we want to change the name in url from q to something then we add parameter 'alias'
async def list_item(q:list[str] = Query(['Hello'], alias='jod')):
    result = {'item id' : [{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q:
        result.update({'q': q})
    return result

# Let's see the hidden query
# Here the Query parameter don't need any value but if we add something then it will show
@app.get('/hidden_query')
async def hidden_q(hidden_query:str | None = Query(None, include_in_schema = False)):
    if hidden_query:
        return {'Hidden Query':'Hidden Query present '+ hidden_query}
    else:
        return{'Hidden Query':'No data found'}
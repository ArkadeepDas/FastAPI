from fastapi import FastAPI, status

# Let's create the app
app = FastAPI()

# Route
# By default status code is 200
# We can see this in /docs
@app.get('/item', status_code=201)
async def create_item(name: str):
    return {'Name' : name}

# We create a empty content
# Same way we can set status code
@app.get('/new_item', status_code=status.HTTP_204_NO_CONTENT)
async def item(pk: str):
    print('pk', pk)
    return pk
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

# Let's create the app
app = FastAPI()

items = {'Food': 'Mango'}

# Route
# If we pass something which is not present then it will show an error and we set some parameters
# It will show them
@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        # We can set headers
        raise HTTPException(status_code = 404,
                            detail = 'Item not found',
                            headers = {'X-error': 'No item present'})
    return {'item': items[item_id]}

# Let's try different method
# We re going to create custome exception
# Inherit from exception
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

# Route
# Here we use custom class for exception
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(status_code = 418,
                        content={'Message': f'Oops! {exc.name} did something'})

# Route
@app.get('/uvicorns/{name}')
async def read_unicorns(name: str):
    if name == 'yolo':
        raise UnicornException(name=name)
    return {'Unicorn_name': name}

#################################################################################
# In the above part what we did is, if the name is 'yolo' it will raise a UnicornException
# We add an exception handler to our app. When we throw a UnicornException, it is handled by unicorn_exception_handler
# We return json responce
# For different exception we can add different exception handler
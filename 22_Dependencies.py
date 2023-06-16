from fastapi import FastAPI, Depends

# Let's create the app
app = FastAPI()

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {'q': q, 'skip': skip, 'limit': limit}

@app.get('/items/')
async def read_items(q: str | None = None, skip: int = 0, limit: int = 100):
    return {'q': q, 'skip': skip, 'limit': limit}

# We want to add same functionality here
# We need a helper function
# Here the helper function is common_parameter()
# Exact same functionality
# We can also nest the Depends
@app.get('/users/')
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
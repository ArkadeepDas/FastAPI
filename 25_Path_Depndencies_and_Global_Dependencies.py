from fastapi import FastAPI, Header, HTTPException, Depends

# Let's create the app
app = FastAPI()

# Create dependency functions
def verify_token(x_token: str = Header(...)):
    if x_token != 'demo token':
        raise HTTPException(status_code = 404, detail = 'Invalid Header')

def verify_key(x_key: str = Header(...)):
    if x_key != 'demo key':
        raise HTTPException(status_code = 404, detail = 'Invalid Key')
    return x_key

# Let's create route and test the Path Dependency
# We can use dependencies in path. Previously we did this with function
@app.get('/items/', dependencies = [Depends(verify_token), Depends(verify_key)])
async def read_item():
    return [{'Tata': 'Harrier', 'Mahindra': 'XUV700'}]

@app.get('/users/', dependencies = [Depends(verify_token), Depends(verify_key)])
async def read_user():
    return [{'Land Rover': 'Defender', 'Lamborgini': 'Aventador'}]
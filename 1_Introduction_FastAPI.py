######################################################################
#################### This is the first basic code ####################

# FastApi requirs uvicorn
from fastapi import FastAPI

# This is a FastAPI app
app = FastAPI()

# First things we need to do is setup a route
# get decoretor for route
# It's a root route
# We can add description of out route
@app.get('/', description='This is our first project on FastAPI')
async def root():
    return {'message' : 'Hello World'}

@app.post('/')
async def post():
    return {'message': 'Message from Post'}

@app.put('/')
async def put():
    return {'message' : 'Message from Put'}

# Command to run: uvicorn file_name:app_name
# Here file_name '1.Introduction_FastAPI.py' and app name is 'app'
# Command: uvicorn 1.IntroductionFastAPI:app
# Flags: --port = we can choose any port we want, default is 8000
# Flags: --reload = update automatically if there is any changes in our code.

# It provides documentations 
# Add /docs in url and execute it. It will provide the output
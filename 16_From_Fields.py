from fastapi import FastAPI, Form
from pydantic import BaseModel
# Let's create the app
app = FastAPI()

# Let's create body
class User(BaseModel):
    user_name: str
    password: str

# Here we are going to see how we are going to pass data in a post request
@app.post('/login')
async def login(user: User):
    return user

# Let's check a from field
# Now we can see in /docs a form
# It will work as form object
@app.post('/user_login')
async def user_login(username: str = Form(...), password: str = Form(...)):
    # Not giving the output of password
    print('Password', password)
    return {'User name': username}
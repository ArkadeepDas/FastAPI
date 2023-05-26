from fastapi import FastAPI, Cookie, Header

# Let's create the app
app = FastAPI()

# Route
@app.get('/items')
# Here we set it as Cookie parameter and Header parameters
async def read_items(cookie_id: str | None = Cookie(None),
                     acc_encoding: str | None = Header(None),
                     user_agent: str | None = Header(None)):
    return {
        'Cookie Id': cookie_id,
        'Accept Encoding': acc_encoding,
        'User Agent': user_agent
    }

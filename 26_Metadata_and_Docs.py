from fastapi import FastAPI

# Let's create a description
description = """
This App helps you to do awesome stuff.

## Items
We can read items

## Users
You will be able to:
* **Create Users** (_Not Implemented_).
* **Read Users** (_Not Implemented_).
"""
# Let's create tags metadata
tag_metadata = [
    dict(name = 'users', description = 'Operations with users'),
    dict(name = 'items', description = 'Manage items')
]

# Let's create the app with description
app = FastAPI(title = 'Demo App', description = description, version = '0.0.1', terms_of_service = 'http://example.com/terms', contact = dict(name = 'Demo app', url = 'http://example.com/terms/contact', email = 'demoapp@example.com'), license_info = dict(name = 'Apache 2.0', url = 'https://www.apache.org/licenses/LICENSES-2.0.html'), openapi_tags = tag_metadata)
# It will give some description about the app
# It will add a 'Terms of service' in /docs \
# It also provide te contacts
# We can add Licence
# After adding the tag_metadata it will show the desciption about it when we use the tag in route.
# If we set doc_url = '/hello', then it will not open in '/docs', it will open in '/hello'

# Routes
# We can add tags to better organize
@app.get('/users/', tags = ['users'])
async def read_users():
    return [{'Name': 'Demo User'}]

@app.get('/items/', tags = ['items'])
async def read_items():
    return [{'Name': 'Demo App'}]
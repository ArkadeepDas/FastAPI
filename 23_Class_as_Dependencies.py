from fastapi import FastAPI, Depends

# Let's create the app
app = FastAPI()

# Try to convert query parameter into a class
demo_db = [{
    'item_name': 'Tata'
}, {
    'item_name': 'Mahindra'
}, {
    'item_name': 'Honda'
}]

# Class of Common Query Parameters
class CommonQueryParameters:

    def __init__(self,
                 q: str | None = None,
                 skip: int = 0,
                 limit: int = 100) -> None:
        self.q = q
        self.skip = skip
        self.limit = limit

# It takes the common parameter as class
@app.get('/items/')
async def read_item(
        common: CommonQueryParameters = Depends(CommonQueryParameters)):
    response = {}
    if common.q:
        response.update({'q': common.q})
    # 0 - 100
    items = demo_db[common.skip:common.skip + common.limit]
    response.update({'items': items})
    return response
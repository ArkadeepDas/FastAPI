from fastapi import FastAPI, Depends, Body

# Let's create the app
app = FastAPI()

def query_extractor(q: str | None = None):
    return q

def query_or_body_extractor(q: str = Depends(query_extractor),
                            last_query: str | None = Body(None)):
    if not q:
        return last_query
    else:
        return q

@app.post('/items/')
async def try_query(query_or_body: str = Depends(query_or_body_extractor)):
    return {'q or body': query_or_body}
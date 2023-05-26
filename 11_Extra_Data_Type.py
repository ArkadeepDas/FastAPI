from fastapi import FastAPI, Body
from uuid import UUID
from datetime import datetime, time, timedelta

# Let's create app
app = FastAPI()

# Route
@app.put('/items/{item_id}')
# Here we are setting it as UUID type
# Now in this moment we are just using datetime as a query parameter
# Now if we use it as a Body parameter then it works like datetime
# Now we can add different kind of body parameters
# Here for path parameter we can't provide normal string, we need to provide UUID type
async def read_items(item_id: UUID,
                     start_date: datetime | None = Body(None),
                     end_date: datetime | None = Body(None),
                     repeat_at: time | None = Body(None),
                     process_after: timedelta | None = Body(None)):
    return {
        'item_id': item_id,
        'start_date': start_date,
        'end_date': end_date,
        'repeat_at': repeat_at,
        'process_after': process_after
    }

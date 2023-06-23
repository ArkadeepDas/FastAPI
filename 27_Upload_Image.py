from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import io

# Let's create the app
app = FastAPI()

# Route
@app.post('/upload/')
async def upload_file(file: UploadFile = File(...)):
    # Read the content of the file
    content = await file.read()
    # Convert content into BytesIO to stream
    image = io.BytesIO(content)
    return StreamingResponse(content=image, media_type = 'image/png')

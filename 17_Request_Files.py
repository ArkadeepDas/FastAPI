from fastapi import FastAPI, File, UploadFile

# Let's create the app
app = FastAPI()

# We are going to tell fastapi that it is a file object. Otherwise we don't see any changes
# It will return the length of the file
@app.post('/files/')
# We can add other parameters like description
async def create_file(file: bytes = File(...)):
    return {'Length of the file': len(file)}

# It will return the name of the file
@app.post('/upload_file/')
async def upload_file(file: UploadFile):
    return {'file name': file.filename}

# We can add multiple files
@app.post('/multiple_files/')
async def multiple_files(files: list[bytes] = File(..., description = 'Multiple files')):
    return {'file sizes': [len(file) for file in files]}
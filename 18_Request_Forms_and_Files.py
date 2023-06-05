from fastapi import FastAPI, File, UploadFile, Form

# Let's create the app
app = FastAPI()

@app.post('/files/')
# Combine of forms and files
async def create_file(file_a: bytes = File(...),
                      file_b: UploadFile = File(...),
                      token: str = Form(...)):
    return {
        'file_size': len(file_a),
        'token': token,
        'file_content_type': file_b.content_type
    }
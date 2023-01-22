from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

import aiofiles
import random
import string
import os
import subprocess

class Story(BaseModel):
    story: str

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/")
async def root():
    return {"message": "backend is a okay"}

def create_job(pdf_path):
    job_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(7))
    os.mkdir(f"public/{job_id}")
    subprocess.Popen(["python3","run.py", job_id, pdf_path])
    return job_id

@app.get("/is-it-done/{id}")
async def is_it_done(id):
    dir = os.listdir(f'public/{id}')
    if len(dir) == 0:
        return {"msg":"Hold on brother"}
    else:
        return {"msg":"PAAAARTTTYYYYY", "href": "http://localhost:8000/public/{id}/game.zip", "download": "game.zip"}

# @app.post("/story-upload")
# async def story_upload(story: Story):
#     id = create_job()
#     return {"job": id}

@app.post("/story-file")
async def story_file(file: UploadFile):
    async with aiofiles.open(f"uploads/{file.filename}", 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
    id = create_job("uploads/{file.filename}")
    return {"job": id}


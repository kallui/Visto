from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/")
async def root():
    return {"message": "backend is a okay"}

# @app.get("/is-it-done/")
# async def is_it_done():

# @app.post("/story-upload")
# async def story_upload():


@app.post("/story-file")
async def story_file(file: UploadFile):
    return {"filename": file.filename}


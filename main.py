import fastapi
import uvicorn
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

#API to print Hello world

app = FastAPI(
    title="Api testing",
    description="Testing HTTP API",
    version="0.1.1",
    openapi_url="/api/v0.1.1/openapi.json",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get api to print hello {name}
@app.get("/hello/{name}")
async def hello_name(name: str):
    return {"Hello": name}

@app.get("/song/{name}")
async def hello_name(name: str):
    if "90" in name:
        return {"Now Playing": "https://www.youtube.com/watch?v=PWyXe6fzsmM"}
    if "80" in name:
        pass

@app.get("/wish/{name}")
async def hello_name(name: str):
    return {"Happy Birthday": name}

#post request to print name
@app.post("/hellopost")
async def hello_name(name: str, age: int):
    return {"Hello": name + " Your age is" + str(age) }

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
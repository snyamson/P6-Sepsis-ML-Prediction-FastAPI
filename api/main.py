from fastapi import FastAPI
from api import api_v1

# Fast API Instance
app = FastAPI()


# / Endpoint
@app.get("/")
async def home():
    return {"Check": "I am Healthy"}


# Include the api version 1
app.include_router(router=api_v1.router, prefix="/api/v1")

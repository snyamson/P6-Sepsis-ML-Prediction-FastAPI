from fastapi import FastAPI

from v1.api_v1 import router as v1_router

# Fast API Instance
app = FastAPI()


# / Endpoint
@app.get("/")
async def home():
    return {"Check": "I am Healthy"}


# Include the api version 1
app.include_router(router=v1_router, prefix="/api/v1")

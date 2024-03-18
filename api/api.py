from fastapi import FastAPI, Request
app = FastAPI()
from . import endpoints
app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "Started application"}

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
# from api.routers import proposal, unit

app = FastAPI()
# app.include_router(proposal.router, prefix="/proposal", tags=["proposals"])
# app.include_router(unit.router, prefix="/unit", tags=["units"])


@app.get("/")
async def root():
    return {"message": "Hello World"}

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/test")
async def test():
    return {"message": "test"}

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return item


@app.post("/")
async def receiveMessage(message: dict) -> dict:
    print(message['message'])
    return {
        "data": { "Message received." }
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, log_level="info", reload=True)

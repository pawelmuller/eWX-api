import uvicorn
from fastapi import FastAPI
from api.routers import proposal

app = FastAPI()
app.include_router(proposal.router, prefix="/proposal", tags=["proposals"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "test"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=True)

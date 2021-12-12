import uvicorn
from fastapi import FastAPI
from api.routers import proposal, unit
from api.utils.db_connection import create_db_engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(proposal.router, prefix="/proposal", tags=["proposals"])
app.include_router(unit.router, prefix="/unit", tags=["units"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "test"}


@app.on_event("startup")
async def startup_event():
    create_db_engine(test=False)

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://ew4.ddns.net:3000",
    "ew4.ddns.net:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=True)

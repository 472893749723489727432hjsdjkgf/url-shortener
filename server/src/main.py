from server.src.routers.url_router import url_router,short_router
from server.src.database.init_db import init_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn




@asynccontextmanager
async def lifespan(app : FastAPI):
    await init_tables()
    print("БД СОЗДАНА!")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(url_router)
app.include_router(short_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,host="localhost")
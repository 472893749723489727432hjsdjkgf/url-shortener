from pathlib import Path
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse,RedirectResponse
from db import sendData,getUrl,init_tables,check_uniqueness_slug
from generate import generate_slug
from contextlib import asynccontextmanager



CLIENT_DIR = Path("../../client").resolve()

class UrlSchema(BaseModel):
    user_url : str

@asynccontextmanager
async def lifespan(app : FastAPI):
    await init_tables()
    print("Таблицы созданы!")
    yield


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return FileResponse(path=CLIENT_DIR/"index.html")

@app.post("/api/short_url")
async def get_short_link(link : UrlSchema):
    slug = generate_slug()
    while  await check_uniqueness_slug(slug):
        slug = generate_slug()
    await sendData(slug,link.user_url)
    return f"http://127.0.0.1:8080/{slug}"


@app.get("/{slug}")
async def redirect(slug: str):
    url = await getUrl(slug)

    if not url or not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise HTTPException(status_code=404, detail="Ссылка не найдена")

    return RedirectResponse(url)





if __name__ == '__main__':
    uvicorn.run("main:app",reload=True,port=8080)
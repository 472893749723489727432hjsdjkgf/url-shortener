from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from server.src.database.crud_db_urls import send_user_data,get_user_url,check_slug
from server.src.generate import generate_slug
from server.src.schemas import UrlSchema,UrlRequest


url_router = APIRouter(prefix="/api/url")
short_router = APIRouter()

@url_router.post("/short_url")
async def create_short_link(user_request : UrlRequest) -> str:
    slug = generate_slug()
    while await check_slug(slug):
        slug = generate_slug()

    url_data = UrlSchema(slug=slug,user_url=user_request.user_url)
    await send_user_data(url_data)
    return f"http://localhost:8080/{slug}"


@short_router.get("/{slug}")
async def redirect(slug: str):
    url = await get_user_url(slug)
    print(f"Redirecting to: {url}")
    return RedirectResponse(url=url)

from server.src.database.models import UrlsModels
from server.src.database.db import session
from server.src.schemas import UrlSchema
from sqlalchemy import select, exists


async def send_user_data(user_data : UrlSchema):
    data = UrlsModels(slug = user_data.slug,user_url = user_data.user_url)
    async with session.begin() as conn:
        conn.add(data)
        await conn.commit()

async def get_user_url(slug : str) ->str:
    query = select(UrlsModels.user_url).where(UrlsModels.slug==slug)
    async with session.begin() as conn:
        res = await conn.execute(query)
        return res.scalar()

async def check_slug(slug : str) -> bool:
    stmt = select(exists().where(UrlsModels.slug == slug))
    async with session.begin() as conn:
        req = await conn.execute(stmt)
        return req.scalar()

"""crud_db"""

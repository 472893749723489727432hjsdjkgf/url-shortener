from server.src.config import settings
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy import select,exists
class Base(DeclarativeBase): pass

engine = create_async_engine(url=settings.URL())
session = async_sessionmaker(bind=engine,expire_on_commit=False)

class Urls(Base):
    __tablename__ = "urls"
    slug : Mapped[str] = mapped_column(primary_key=True)
    user_url : Mapped[str]

async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def sendData(slug : str,url : str):
    data = Urls(slug=slug,user_url=url)
    async with session.begin() as conn:
        conn.add(data)
        await conn.commit()

async def check_uniqueness_slug(slug : str) ->bool:
    stmt = select(exists().where(Urls.slug == slug))
    async with session.begin() as conn:
        req = await conn.execute(stmt)
        return req.scalar()


async def getUrl(slug : str) ->str:
    query = select(Urls).where(Urls.slug==slug)
    async with session.begin() as conn:
        req = await conn.execute(query)
        url = req.scalar_one_or_none()
        if url is None:
            return "Ошибка со слагом"
        return url.user_url


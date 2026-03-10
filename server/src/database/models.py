from server.src.database.db import Base
from sqlalchemy.orm import Mapped,mapped_column


class UrlsModels(Base):
    __tablename__ = "urls"
    id : Mapped[int]  = mapped_column(primary_key=True)
    slug : Mapped[str]
    user_url : Mapped[str]



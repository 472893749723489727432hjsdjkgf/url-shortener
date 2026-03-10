from pydantic import BaseModel


class UrlSchema(BaseModel):
    user_url : str
    slug : str


class UrlRequest(BaseModel):
    user_url : str
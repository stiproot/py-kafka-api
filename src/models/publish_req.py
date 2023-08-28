from pydantic import BaseModel


class PublishReq(BaseModel):
    key: str
    payload: str

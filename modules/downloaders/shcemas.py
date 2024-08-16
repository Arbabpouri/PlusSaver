from pydantic import BaseModel


class MediaDownloaded(BaseModel):
    PATH: str | None = None
    TITLE: str | None = None
    CAPTION: str | None = None
    
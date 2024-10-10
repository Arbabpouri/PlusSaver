from pydantic import BaseModel


class MediaDownloaded(BaseModel):
    MEDIA: str | bytes |None = None
    TITLE: str | None = None
    CAPTION: str | None = None
    RESULT: bool | None = None


class MediasDownloaded(BaseModel):
    MEDIAS: list[MediaDownloaded] | None = None

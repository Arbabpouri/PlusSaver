from .shcemas import MediaDownloaded
from .base import BaseDownloader

class Spotify(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
    

    
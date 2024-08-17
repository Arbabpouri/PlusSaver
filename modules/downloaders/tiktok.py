from .shcemas import MediaDownloaded
from .base import BaseDownloader

class TikTok(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        
    
    def download_post(self) -> MediaDownloaded:
        pass

    
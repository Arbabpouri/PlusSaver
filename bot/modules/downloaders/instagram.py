import aiohttp
from .shcemas import MediaDownloaded
from .base import BaseDownloader

class Instagram(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.__api_url = "https://submagic-free-tools.fly.dev/api/instagram-download"
        self.__data = {
            "url": str(self.url)
        }
        
        self.__headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
        }

    async def download_media(self) -> MediaDownloaded:
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url=self.__api_url, data=self.__data, headers=self.__headers) as response:
                
                if response.status == 200:
                    response_data = await response.json()
                    download_url = response_data.get('downloadLink')
                    caption = response_data.get('videoTitle')
                    
                    if download_url:
                        return MediaDownloaded(MEDIA=download_url, CAPTION=caption, RESULT=True, TITLE='Instagram Video')
                    
                    return MediaDownloaded()
            
                return MediaDownloaded(RESULT=False)

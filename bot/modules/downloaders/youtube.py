import requests
import aiohttp
from pydantic import BaseModel
from .shcemas import MediaDownloaded
from .base import BaseDownloader



class DownloadResponseMedia(BaseModel):
    formatId: int
    label: str
    type: str
    ext: str
    width: int | None = None
    height: int | None = None
    url: str
    bitrate: int
    fps: int | None = None
    audioQuality: str | None = None
    audioSampleRate: str | None = None
    mimeType: str
    duration: int
    
    
class DownloadResponseMedias(BaseModel):
    defaultFormatId: int
    duration: str
    formats: list[DownloadResponseMedia]
    thumbnailUrl: str
    title: str


class Youtube(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.__api_url = "https://submagic-free-tools.fly.dev/api/youtube-info"
        self.__data = {
            "url": str(self.url)
        }
        
        self.__headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
        }
                
    async def download_video(self) -> MediaDownloaded:
        
        async with aiohttp.ClientSession() as session:
                
            async with session.post(url=self.__api_url, data=self.__data, headers=self.__headers) as response:
            
                if response.status == 200:
                    
                    try:
                        
                        data = await response.json()                        
                        medias = DownloadResponseMedias(**data)
                        
                        for media in medias.formats:
                            if media.type == 'video_with_audio' and  media.duration < 1000000:
                                title = medias.title
                                url = media.url
                                del medias
                                video = requests.get(url)
                                async with session.get(url) as video:
                                    
                                    if video.status == 200:
                                        file_path = fr"./download/video/{title}.mp4"
                                        with open(file_path, "wb") as file:
                                            file.write(await video.read())
                                        del video
                                        return MediaDownloaded(MEDIA=file_path, TITLE=title, RESULT=True)
                            
                            return MediaDownloaded(RESULT=None)
                                        
                    except Exception as e:
                        print("Error is Youtube download media :", e)
        
        return MediaDownloaded(RESULT=False)
        

        

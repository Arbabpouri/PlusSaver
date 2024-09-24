from .shcemas import MediaDownloaded
from .base import BaseDownloader
from bs4 import BeautifulSoup
import requests


class Pinterest(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.__image_class = "hCL kVc L4E MIw"
        self.__caption_class = "tBJ dyH iFc sAJ X8m zDA IZT swG"
        self.__video_class = ""
        
    async def download_image(self) -> MediaDownloaded:
        
        try:
            
            response = requests.get(self.url)
            
            if response.status_code != 200:
                return MediaDownloaded(RESULT=None)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            media = soup.find("video",class_="hwa kVc MIw L4E")
            if media:
                media = media.get('src')
                media = media.replace("hls","720p").replace("m3u8","mp4")
            else:
                media = soup.find("img", attrs={"class": self.__image_class})
                if media:
                    media = media.get('src')
                    
            if not media:
                return MediaDownloaded()
            
            caption = soup.find_all("span", attrs={"class": self.__caption_class})
            if caption:
                caption = caption[-1].text
            else:
                caption = "no caption"
            
            if media:
                
                media = MediaDownloaded(
                    MEDIA=media,
                    TITLE=soup.select_one('title').text,
                    CAPTION=caption,
                    RESULT=True
                )
            
            else:            
                media = MediaDownloaded(RESULT=None)
                    
        except Exception as e:
            print(f"Error fetching medias from {self.url}: {e}")
            media = MediaDownloaded(RESULT=False)
            
        return media

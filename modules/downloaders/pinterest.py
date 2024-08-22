from .shcemas import MediaDownloaded
from .base import BaseDownloader
from bs4 import BeautifulSoup
import requests


class Pinterest(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.__image_class = "hCL kVc L4E MIw"
        self.__caption_class = "tBJ dyH iFc sAJ X8m zDA IZT swG"
        
    def download_image(self) -> MediaDownloaded:
        
        try:
            
            response = requests.get(self.url)
            
            if response.status_code != 200:
                return MediaDownloaded(RESULT=None)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            image = soup.find("img", attrs={"class": self.__image_class}).get('src') or None
            caption = soup.find_all("span", attrs={"class": self.__caption_class})[-1].text or "no caption"
            
            if image:
                
                media = MediaDownloaded(
                    MEDIA=image,
                    TITLE=soup.select_one('title').text,
                    CAPTION=caption,
                    RESULT=True
                )
            
            else:            
                media = MediaDownloaded(RESULT=None)
                    
        except Exception as e:
            print(f"Error fetching images from {self.url}: {e}")
            media = MediaDownloaded(RESULT=False)
            
        return media

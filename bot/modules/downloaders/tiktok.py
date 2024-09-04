from .shcemas import MediaDownloaded
from .base import BaseDownloader
from bs4 import BeautifulSoup
from uuid import uuid4
import requests


class TikTok(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.__api_url = "https://ssstik.io/abc?url=dl"
        self.__a_class_download_url = "pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark vignette_active notranslate"
        self.__p_class_caption = "maintext"
        self.__header_tiktokcdn = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            # سایر هدرهای مورد نیاز
        }
        self.__header_ssstik = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
            
        self.__download_post_data = {
            "id": self.url,
            "locale": "en",
            "tt": "MnZQcWQ2",
        }
    
    async def download_post(self) -> MediaDownloaded:
        
        try:
            
            request = requests.Session()
                        
            response =  request.post(self.__api_url, headers=self.__header_ssstik, data=self.__download_post_data)

            if response.status_code != 200:
                return MediaDownloaded(RESULT=None)
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            download_url = soup.find("a", attrs={"class": self.__a_class_download_url})
            if download_url:
                                
                video = request.get(download_url.get("href"), headers=self.__header_tiktokcdn, timeout=10) or None
                
                if video and video.status_code == 200:
                    
                    
                    file_path = rf"{self.save_video_path}/{uuid4()}.mp4"
                    
                    with open(file_path, "wb") as file:
                        file.write(video.content)
                                        
                    title = soup.find("h2")
                    caption = soup.find("p", attrs={"class": self.__p_class_caption})
                    
                    media = MediaDownloaded(
                        MEDIA=file_path,
                        TITLE=title.text,
                        CAPTION=caption.text,
                        RESULT=True
                    )
                    
                else:
                    
                    media = MediaDownloaded(RESULT=False)
            else:
                
                media = MediaDownloaded(RESULT=False)
                
                    
        except Exception as e:
            print(f"Error fetching images from {self.url}: {e}")
            media = MediaDownloaded(RESULT=False)
            
        return media

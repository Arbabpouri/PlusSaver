from .shcemas import MediaDownloaded
from .base import BaseDownloader
from bs4 import BeautifulSoup
import requests


class TikTok(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.__video_preload = "auto"
        
    
    def download_post(self) -> MediaDownloaded:
        
        try:
            
            
            
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
            }
            info = requests.get("https://tiktok.com", headers=header)
            print(info.cookies.items())
            response = requests.get(self.url, headers=info.request.headers, cookies=info.cookies)
            
            if response.status_code != 200:
                return MediaDownloaded(RESULT=None)
                        
            soup = BeautifulSoup(response.text, 'html.parser')            
            
            # video = soup.find("video", """attrs={"preload": self.__video_preload}""")
            video = soup.find_all("video")
            
            print(video)
            return
            
            if video and video.get('src'):
                # caption = soup.find_all("span", attrs={"class": self.__caption_class})[-1].text or "no caption"
                media = MediaDownloaded(
                    PATH=video,
                    TITLE=soup.select_one('title').text,
                    CAPTION="caption",
                    RESULT=True
                )
            
            else:            
                media = MediaDownloaded(RESULT=None)
                    
        except Exception as e:
            print(f"Error fetching images from {self.url}: {e}")
            media = MediaDownloaded(RESULT=False)
            
        return media


# a = TikTok('https://www.tiktok.com/player/v1/6718335390845095173').download_post()


# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# # تنظیمات Chrome برای حالت Headless
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # حالت بدون رابط کاربری
# chrome_options.add_argument("--no-sandbox")  # برای امنیت بیشتر
# chrome_options.add_argument("--disable-dev-shm-usage")  # جلوگیری از مشکلات حافظه
# chrome_options.add_argument("--disable-gpu")  # غیرفعال کردن GPU

# # ایجاد سرویس Chrome
# service = Service(ChromeDriverManager().install())

# # ایجاد وب‌درایور
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # بارگذاری صفحه
# driver.get("https://www.tiktok.com/@cyrusthevirustv/video/6915747896285613318")

# # انجام عملیات مورد نظر (مثلاً استخراج عنوان صفحه)
# print(driver.find_element(By.TAG_NAME, "video").get_attribute("src"))

# # بستن درایور
# driver.quit()




   

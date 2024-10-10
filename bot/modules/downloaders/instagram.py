import aiohttp
import json
from asyncio import sleep
from uuid import uuid4
from .shcemas import MediaDownloaded, MediasDownloaded
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
                    del response
                    del response_data
                    async with session.get(download_url) as media:
                        if media.status == 200:
                            
                            media_path = self.save_video_path + f"/{uuid4()}.mp4"
                            with open(media_path, 'wb') as file:
                                file.write(await media.read())
                            
                            return MediaDownloaded(MEDIA=media_path, CAPTION=caption, RESULT=True, TITLE='Instagram Video')
                    
                        return MediaDownloaded()
            
                return MediaDownloaded(RESULT=False)


class InstagramV2(BaseDownloader):
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.__api_url_get_job = "https://app.publer.io/hooks/media"
        self.__api_url_get_medias = "https://app.publer.io/api/v1/job_status"
        self.__data = {
            "url": self.url
        }
        
        self.__data = json.dumps(self.__data, indent=4)
        self.__headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36",
            "Referer": "https://publer.io/",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Postman-Token": "7215ab1c-377c-4f9f-bda9-548a989483c4",
            "Host": "app.publer.io",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Content-Length": str(len(self.__data)),
        }
        
    async def download_media(self) -> MediaDownloaded:
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url=self.__api_url_get_job, data=self.__data, headers=self.__headers) as get_job_response:
                if get_job_response.status != 200:
                    return MediaDownloaded(RESULT=False)
                
                job_id = await get_job_response.json()
                job_id = job_id.get("job_id")
                
                while True:
                                
                    async with session.get(url=self.__api_url_get_medias + f"/{job_id}") as get_media_response:

                        if get_media_response.status != 200:
                            return MediaDownloaded(RESULT=None)
                        
                        medias = MediasDownloaded()
                        medias.MEDIAS = []
                        medias_info = await get_media_response.json()

                        if medias_info.get("status") == "working":
                            await sleep(2)
                            continue
                        
                        for media in medias_info.get("payload"):
                            async with session.get(media.get("path")) as m:
                                ext = "mp4" if media.get("type") == "video" else "jpg"
                                path = f"{self.save_video_path}/{uuid4()}.{ext}"
                                with open(path, "wb") as file:
                                    file.write(await m.read())
                            media_obj = MediaDownloaded(
                                MEDIA=path,
                                TITLE="Instagram Media",
                                CAPTION=media.get("caption"),
                                RESULT=True
                            )
                            medias.MEDIAS.append(media_obj)
                                                    
                        return medias
        
        return MediaDownloaded(RESULT=None)
                    
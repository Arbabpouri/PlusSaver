from yt_dlp import YoutubeDL
from typing import Optional
from .shcemas import MediaDownloaded
from ..enums import YoutubeVideResoloution
from .base import BaseDownloader

class Youtube(BaseDownloader):
    
    def __init__(self, url: str, video: Optional[bool] = True) -> None:
        super().__init__(url)
        self.__coockies_path = r"./config/cookies.txt"
        self.__ytdlp_opts = {
            'cookiefile': './config/cookies.txt',
            'format': 'best' if video else 'mp3',
            'quiet': True,
        }

    def get_resolutions(self) -> list:
        """get_resolutions methdo for get video resolutions
        
        >>> Youtube('url').get_resolutions()

        Returns:
            list: a list of Stream object
        """
        pass
        
    def download_music(self) -> MediaDownloaded:
        """_summary_

        Returns:
            MediaDownloaded: _description_
        """
        
        pass
                
    def download_video(self, resolution: Optional[str] = YoutubeVideResoloution.R_144P.value) -> MediaDownloaded:
        """download_video method for download vide from youtube with custom resolution
        
        >>> Youtube('url').download_video(resolution=YoutubeVideResoloution.R_144P.value)
        or
        >>> Youtube('url').download_video(resolution='720p')

        Args:
            resolution (Optional[str], optional): _description_. Defaults to "144p".

        Returns:
            MediaDownloaded: ...
        """
        media = MediaDownloaded()
        try :
            with YoutubeDL(self.__ytdlp_opts) as ydl:
                
                info_dict = ydl.extract_info(self.url, download=False)
                
                video_url = info_dict.get('url', None)
                title = info_dict.get('title', None)
                description = info_dict.get('description', None)
                
                if video_url:
                    media = MediaDownloaded(
                        MEDIA=video_url,
                        TITLE=title,
                        CAPTION=description,
                        RESULT=True
                    )
                    
                else:
                    media = MediaDownloaded(RESULT=None)
        
        except Exception as e:
            print(e)
            media = MediaDownloaded(RESULT=False)
            
        return media

        

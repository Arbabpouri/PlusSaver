from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from typing import Optional
from .shcemas import MediaDownloaded
from ..enums import YoutubeVideResoloution
from .base import BaseDownloader

class Youtube(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.youtube_client = YouTube(self.url)

    def get_resolutions(self) -> list:
        """get_resolutions methdo for get video resolutions
        
        >>> Youtube('url').get_resolutions()

        Returns:
            list: a list of Stream object
        """
        resolutions = self.youtube_client.streams.all()
        return resolutions

    def download_music(self) -> MediaDownloaded:
        """_summary_

        Returns:
            MediaDownloaded: _description_
        """
        
        try:
            music = self.youtube_client.streams.get_audio_only(subtype='mp3').download(self.save_music_path)
            media = MediaDownloaded(MEDIA=music, TITLE=self.youtube_client.title, CAPTION=self.youtube_client.description, RESULT=True)
        
        except VideoUnavailable:
            media = MediaDownloaded(RESULT=None)
        
        except Exception as e:
            print("Error in download_video method: ", e)
            media = MediaDownloaded(RESULT=False)
        
        return media

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
        
        try:
            video = self.youtube_client.streams.get_by_resolution(resolution).download(self.save_video_path)
            media = MediaDownloaded(MEDIA=video, TITLE=self.youtube_client.title, CAPTION=self.youtube_client.description, RESULT=True)
        except VideoUnavailable:
            media = MediaDownloaded(RESULT=None)
        
        except Exception as e:
            print("Error in download_video method: ", e)
            media = MediaDownloaded(RESULT=False)
        
        return media
        

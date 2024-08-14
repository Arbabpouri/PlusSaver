from pytube import YouTube
from typing import Optional
from ..regexs import Regexs


class Youtube:
    
    def __init__(self, url: str) -> None:
        self.url = url
        self.youtube_client = YouTube(self.url)

    def get_resolutions(self) -> list:
        """get_resolutions methdo for get video resolutions
        
        >>> Youtube('url').get_resolutions()

        Returns:
            list: a list of Stream object
        """
        resolutions = self.youtube_client.streams.all()
        return resolutions

    def download_music(self):
        pass

    def download_video(self, resolution: Optional[str] = "144p") -> str | None:
        """download_video methdo for download vide from youtube with custom resolution
        
        >>> Youtube('url').download_video(resolution='720p')

        Args:
            resolution (Optional[str], optional): _description_. Defaults to "144p".

        Returns:
            str | None: if str returned it is video path, also 
        """
        try:
            video = self.youtube_client.streams.get_by_resolution(resolution).download(r'./youtube/videos/')
            return video
        except Exception as e:
            print("Error in download_video method: ", e)

Youtube('123').download_video()
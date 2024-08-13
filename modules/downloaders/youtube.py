from pytube import YouTube
from ..regexs import Regexs


class Youtube:
    
    def __init__(self, url: str) -> None:
        self.url = url

        if not Regexs(self.url).youtube:
            raise ValueError("url not match")

    def get_resolotions(self) -> list:
        pass

    def download_music(self):
        pass

    def download_video(self, resolotion):
        pass

    
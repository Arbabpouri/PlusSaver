from abc import abstractmethod, ABC


class BaseDownloader(ABC):
    
    @abstractmethod
    def __init__(self, url: str) -> None:
        self.url = url
        self.save_image_path = r"./download/image"
        self.save_video_path = r"./download/video"
        self.save_music_path = r"./download/music"
        
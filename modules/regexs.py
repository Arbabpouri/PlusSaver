import re


class Regexs:


    def __init__(self, url: str) -> None:
        self.url = url
        
        self.youtube_regex = r""
        self.soundcloud_regex = r""
    
    @property
    def is_instagram(self) -> bool:
        pass

    @property
    def is_youtube(self) -> bool:
        return bool(re.match(pattern=self.youtube_regex, string=self.url))

    @property
    def is_soundcloud(self) -> bool:
        return bool(re.match(pattern=self.soundcloud_regex, string=self.url))

    @property
    def is_spotify(self) -> bool:
        pass

    @property
    def is_tiktok(self) -> bool:
        pass

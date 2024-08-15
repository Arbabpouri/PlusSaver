import re


class Regexs:


    def __init__(self, url: str) -> None:
        self.url = url
        
        self.youtube_regex = r""
        self.soundcloud_regex = r""
        self.spotify_regex = r""
        self.tiktok_regex = r""
        self.instagram_story_regex = r""
        self.instagram_reels_regex = r""
        self.instagram_post_regex = r""
    
    @property
    def is_instagram(self) -> bool:
        return bool(
            re.match(pattern=self.instagram_story_regex, string=self.url) or
            re.match(pattern=self.instagram_reels_regex, string=self.url) or
            re.match(pattern=self.instagram_post_regex, string=self.url)
        )
        
    @property 
    def is_instagram_reels(self) -> bool:
        return bool(re.match(pattern=self.instagram_reels_regex, string=self.url))
    
    @property 
    def is_instagram_story(self) -> bool:
        return bool(re.match(pattern=self.instagram_story_regex, string=self.url))
    
    @property 
    def is_instagram_post(self) -> bool:
        return bool(re.match(pattern=self.instagram_post_regex, string=self.url))

    @property
    def is_youtube(self) -> bool:
        return bool(re.match(pattern=self.youtube_regex, string=self.url))

    @property
    def is_soundcloud(self) -> bool:
        return bool(re.match(pattern=self.soundcloud_regex, string=self.url))

    @property
    def is_spotify(self) -> bool:
        return bool(re.match(pattern=self.spotify_regex, string=self.url))

    @property
    def is_tiktok(self) -> bool:
        return bool(re.match(pattern=self.tiktok_regex, string=self.url))

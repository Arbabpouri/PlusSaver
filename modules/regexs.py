import re


class Regexs:


    def __init__(self, url: str) -> None:
        self.url = url
        
        self.youtube_regex = r"https?:\/{2}(m\.|www\.)?(youtube\.com|youtu\.be)(\/[a-z0-9?=/]*)?"
        self.soundcloud_regex = r"^(?:https?:\/\/)((?:www\.)|(?:m\.))?soundcloud\.com\/[a-z0-9](?!.*?(-|_){2})[\w-]{1,23}[a-z0-9](?:\/.+)?$"
        self.spotify_regex = r"^(spotify:|https:\/\/[a-z]+\.spotify\.com\/)"
        self.tiktok_regex = r"(?:http(?:s)?:\/\/)?(?:(?:www)\.(?:tiktok\.com)(?:\/)(?!foryou)(@[a-zA-z0-9]+)(?:\/)(?:video)(?:\/)([\d]+)|(?:m)\.(?:tiktok\.com)(?:\/)(?!foryou)(?:v)(?:\/)?(?=([\d]+)\.html))"
        self.instagram_story_regex = r"https?:\/\/(?:www.)?instagram.com\/stories\/([^\/?#&]+).*"
        self.instagram_reels_regex = r"https?:\/\/(?:www.)?instagram.com\/reel\/([^\/?#&]+).*"
        self.instagram_post_regex = r"https?:\/\/(?:www.)?instagram.com\/p\/([^\/?#&]+).*"
        self.pinterest_regex = r"^(http(s?):\/{2})?(w{3}.)?pinterest\.com/pin/\d+"
    
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

    @property
    def is_pinterest(self) -> bool:
        return bool(re.match(pattern=self.pinterest_regex, string=self.url))
    
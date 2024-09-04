from instaloader import Instaloader, Post, Story, Profile
from .shcemas import MediaDownloaded
from .base import BaseDownloader

class Instagram(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.instagram_client = Instaloader()
        
    async def download_post(self) -> MediaDownloaded:
        """_summary_

        Returns:
            MediaDownloaded: _description_
        """
        
        
        # a = self.instagram_client.download_post(Post(self.instagram_client.context))
        # post = Post.from_shortcode(self.instagram_client.context, self.url.split("/")[-2])
        # print(post)
            
        media = MediaDownloaded(
            MEDIA=self.url.replace("instagram.com", "ddinstagram.com"),
            TITLE="t",
            CAPTION="ca",
            RESULT=True
        )
        
        return media
    
    async def download_profile(self) -> MediaDownloaded:
        """_summary_

        Returns:
            MediaDownloaded: _description_
        """
        
        pass
    
    async def download_story(self) -> MediaDownloaded:
        """_summary_

        Returns:
            MediaDownloaded: _description_
        """
        
        pass
        

    
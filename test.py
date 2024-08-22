import yt_dlp

while True:
    url = input("Enter the YouTube video URL: ")

    ydl_opts = {
        # "format": "bestvideo+bestaudio/best",
        # "outtmpl": "%(title)s.%(ext)s",
        # "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL() as ydl:
        ydl.download([url])
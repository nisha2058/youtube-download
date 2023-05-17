from pytube import YouTube
import sys
import os

link=sys.argv[1]
yt =YouTube(link)
print("Title: ", yt.title)
print("Views: ",yt.views)

video=yt.streams.get_highest_resolution()

cwd=os.getcwd()
download_path=os.path.join(cwd,video.title + ".mp4")

video.download(download_path)
print('video downloaded successfully')



from pytube import YouTube
import os

from sys import argv


def download(link):
    
    yt= YouTube(link)
    yd= yt.streams.get_highest_resolution()
    folder_name = "D:/MyVideo"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    
    return yd.download(folder_name)




    






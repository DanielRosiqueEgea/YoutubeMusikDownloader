
import sys, subprocess; 
subprocess.run([sys.executable, '-m', 'pip', 'install', 'pytube3'])
#subprocess.run([sys.executable, '-m', 'pip', 'install', 'os_sys'])

from pytube import YouTube
from pytube import Playlist
import os

PATH = "E:\\Musikote"
link = input("Enter the link: ")

playlist = Playlist(link)

allMusik =os.listdir(PATH)

allMusik += os.listdir(PATH+"\\Prueba")


for link in playlist.video_urls:
    existed =0
    yt = YouTube(link)

    for musik in allMusik:
        if yt.title in musik:
            print("Ya existía: ",yt.title)
            existed=1
    if existed == 1:
        continue
    try:
        ys = yt.streams.filter(only_audio=True,mime_type="audio/webm").first()
    except:
        try: 
            ys = yt.streams.first()
        except:
            continue
    out_file = ys.download(PATH+"\\Prueba")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    try:
        os.rename(out_file, new_file)     
        print(yt.title + " has been successfully downloaded.")
    except:
        os.remove(out_file)
        print("Error al crear el archivo")
    # result of success
    
print("Existian: ", existed," Canciones")
# print(yt.streams.filter(only_audio=True))

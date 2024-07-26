
import sys
# , subprocess; 
# subprocess.run([sys.executable, '-m', 'pip', 'install', 'pytube3'])
#subprocess.run([sys.executable, '-m', 'pip', 'install', 'os_sys'])

from tqdm import tqdm 
from pytubefix import YouTube
from pytube import Playlist
import os

PATH = "C:\\Users\\roxon\\Desktop\\Programación\\YoutubeMusikDownloader\\Musica"
# link = input("Enter the link: ")
link = "https://youtube.com/playlist?list=PLVD7ep3F1HnCm06kgk13XkMtnnACYhDil&si=IDkDjUlHxLcVZNaN"
# link = "https://www.youtube.com/playlist?list=PLR72LBjlvus6xDV7r6qUHy2adTH2On6UC"
# link ="https://www.youtube.com/watch?v=HkpsOu0iogk&list=PLR72LBjlvus6xDV7r6qUHy2adTH2On6UC&index=1"
# yt = YouTube(link)
# print(yt.title)
# sys.exit(0)
playlist = Playlist(link)
# print(playlist)
allMusik =os.listdir(PATH)

allMusik += os.listdir(PATH)

progress_bar = tqdm(total=len(playlist.video_urls), desc="Procesando Canciones", ncols=100)
existing_musik =0
downloaded = 0
progress_bar.set_postfix({"downloaded": downloaded})
for link in playlist.video_urls:
    existed =0
    yt = YouTube(link)
    progress_bar.set_description(f'{yt.title} Reference fetched')
    # print(yt.streams)
    # sys.exit()
    
    progress_bar.refresh()
    for musik in allMusik:
        if yt.title in musik:
            # print("Ya existía: ",yt.title)
            progress_bar.set_description(f'{yt.title} Already existed')
            
            progress_bar.refresh()  
            existed=1
            existing_musik +=1
    if existed == 1:
        progress_bar.update(1)
        progress_bar.refresh()
        continue
    try:
        ys = yt.streams.filter(only_audio=True,mime_type="audio/webm").first()
        progress_bar.set_description(f'{yt.title} Stream fetched')
        progress_bar.refresh()
    except:
        try: 
            ys = yt.streams.first()
            progress_bar.set_description(f'{yt.title} Alternative Stream fetched')
            progress_bar.refresh()
        except:
            progress_bar.set_description(f'{yt.title}  Not Found')
            progress_bar.update(1)
            progress_bar.refresh()
            continue
    try:
        out_file = ys.download(PATH)
    except:
        progress_bar.set_description(f'{yt.title}  Not Found')
        progress_bar.update(1)
        progress_bar.refresh()
        continue
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    progress_bar.set_description(f'Saving {yt.title}')
    try:
        os.rename(out_file, new_file)   
        progress_bar.set_description(f'{yt.title}  has been successfully downloaded.')
        progress_bar.refresh()
        # print(yt.title + " has been successfully downloaded.")
        # downloaded+=1
    except:
        os.remove(out_file)
        progress_bar.set_description(f'Error al crear el archivo "+ {yt.title}')
        progress_bar.refresh()
        # print("Error al crear el archivo")
    # result of success
    downloaded+=1
    progress_bar.set_postfix({"downloaded": downloaded})
    progress_bar.update(1)
    progress_bar.refresh()
    
print("Existian: ", existing_musik," Canciones")
# print(yt.streams.filter(only_audio=True))

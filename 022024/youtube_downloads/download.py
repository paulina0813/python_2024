from pytube import YouTube

url = 'https://www.youtube.com/watch?v=iWG6apzIWAk'

youtube = YouTube(url)

stream = youtube.streams.get_highest_resolution()

download_path = '/Users/Pruebas/Desktop/curso_python_24_01/python_2024/022024/youtube_downloads'
file_name = 'Stick_Season_Noah_Kahan.mp4'
stream.download()
#install pytube first 
from pytube import YouTube
link = input("Enter the link: ")
yt = YouTube(link)
print("Title: ",yt.title)
yt.streams.filter(file_extension='mp4')
#for video tag 
stream = yt.streams.get_by_itag(22)
# for downloding 
stream.download()

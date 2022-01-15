from pytube import YouTube
import os
os.system("cls")
link = input("Enter the link: ")
yt = YouTube(link)
print("""Choose the Qualitiy:
Press 1 for low quality.
press 2 for medium quality .
press 3 for high quality.
""")
a=input(":  ")
if a==1:
    print("""what do you want to download 
    input a for audio 
    input v for video """)
    p=input(":  ")
    if  p=="a" or p=="A":
         z=input("input the name of file plz include .mp3 at last:  ")
         print(f'Downloding: {yt.title}')
         yt.streams.first().download()
         os.rename(yt.streams.first().default_filename, z )
         print("DONE")
         os.system("cls")
    elif p=="V" or p=="v":
         z=input("input the name of file plz include .mp4 at last:   ")
         print(f'Downloding: {yt.title}')     
         yt.streams.get_by_itag(18).download()
         os.rename(yt.streams.get_by_itag(18).default_filename, z )
         print("DONE")
         os.system("cls")
    else:
         print("Wrong cammand")

         os.system("cls")
elif a==2:
    print("""what do you want to download 
    input a for audio 
    input v for video """)
    p=input(":  ")
    if  p=="a" or p=="A":
         z=input("input the name of file plz include .mp3 at last:  ")  
         print(f'Downloding: {yt.title}')
         yt.streams.first().download()
         os.rename(yt.streams.first().default_filename, z )
         print("DONE")
         os.system("cls")
    elif p=="V" or p=="v":
         z=input("input the name of file plz include .mp4 at last:   ")
         print(f'Downloding: {yt.title}')     
         yt.streams.get_by_itag(22).download()
         os.rename(yt.streams.get_by_itag(137).default_filename, z )
         print("DONE")
         os.system("cls")
    else:
         print("Wrong cammand")
         os.system("cls")
elif a==3:
    print("""what do you want to download 
    input a for audio 
    input v for video """)
    p=input(":  ")
    if  p=="a" or p=="A":
         z=input("input the name of file plz include .mp3 at last:  ")  
         print(f'Downloding: {yt.title}')
         yt.streams.first().download()
         os.rename(yt.streams.first().default_filename, z )
         print("DONE")
         os.system("cls")
    elif p=="V" or p=="v":
         z=input("input the name of file plz include .mp4 at last:   ")
         print(f'Downloding: {yt.title}')     
         yt.streams.get_by_itag(22).download()
         os.rename(yt.streams.get_by_itag(137).default_filename, z )
         print("DONE")
         os.system("cls")
    else:
         print("Wrong cammand")
         os.system("cls")
else:
     print("Wrong cammand")
     os.system("cls")
  

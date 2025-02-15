import os
import re
unmastered_folder = "C:\\Users\\super\\Desktop\\Chinese symphonic"
download_folder = "C:\\Users\\super\\Downloads\\"
mastered_folder = "C:\\Users\\super\\Desktop\\Mastered"

song_array = []
def populateArray():
    global song_array
    for file_name in os.listdir(unmastered_folder):
        if file_name.lower().endswith('.mp3') and os.path.isfile(os.path.join(unmastered_folder, file_name)):
            song_name = re.sub(r'\.mp3$', '', file_name, flags=re.IGNORECASE)
            song_array.append(song_name)
#populateArray()
#for song_name in song_array:
            #Upload track
            # Construct the full path of the song
    #song_path = os.path.join(unmastered_folder, song_name)
#    print (song_name)

from datetime import date

today_date = date.today()
today_date = today_date.strftime("%Y-%m-%d")
print(today_date)
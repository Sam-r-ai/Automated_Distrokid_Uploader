import webupload
import artcreator
import combined
import FileCleaner

import Songnamechanger
# Asks me for an album theme and it will make the art for me and also Name the album cover that and makes names based on that

albumTheme = input("Enter Album Theme: ")
ready_to_upload = True

folder_path = "C:\\Users\\super\\Desktop\\InputMusicFolder"
output_folder = "C:\\Users\\super\\Desktop\\OutputMusicFolder"

# Create the art
image_path = artcreator.generate_album_cover(albumTheme)

Songnamechanger.process_folder_and_rename_songs(folder_path, output_folder, albumTheme)

webupload.open_distrokid(albumTheme, ready_to_upload, image_path)

print ("Press enter to clean folders and finish")
FileCleaner.clear_workfolders(albumTheme)
import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_files(src_folder, dst_folder):
    if os.path.exists(src_folder):
        for filename in os.listdir(src_folder):
            src_file = os.path.join(src_folder, filename)
            dst_file = os.path.join(dst_folder, filename)
            if os.path.isfile(src_file):
                shutil.move(src_file, dst_file)

def clear_workfolders(folder_name):
    # Define paths
    desktop_path = "C:\\Users\\super\\Desktop"
    garbo_folder = os.path.join(desktop_path, folder_name)
    output_music_folder = os.path.join(desktop_path, "OutputMusicFolder")
    input_music_folder = os.path.join(desktop_path, "InputMusicFolder")
    generated_album_covers_folder = os.path.join(desktop_path, "GeneratedAlbumCovers")
    used_files_folder = os.path.join(desktop_path, "UsedFiles")
    
    # Create Garbo folder
    create_directory(garbo_folder)
    
    # Move files to Garbo folder
    move_files(output_music_folder, garbo_folder)
    move_files(input_music_folder, garbo_folder)
    move_files(generated_album_covers_folder, garbo_folder)
    
    # Create UsedFiles folder if it doesn't exist
    create_directory(used_files_folder)
    
    # Move Garbo folder to UsedFiles folder
    shutil.move(garbo_folder, used_files_folder)
    
    print("Files moved successfully.")


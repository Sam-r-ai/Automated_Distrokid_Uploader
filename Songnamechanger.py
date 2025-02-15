import os
import re
from openai import OpenAI
import shutil
from dotenv import load_dotenv
# Initialize the OpenAI client

# Load environment variables from .env file
load_dotenv()

# Read API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)


def get_song_names(theme, num_songs):
    messages = [
        {"role": "system", "content": "You are a wildly imaginative assistant helping the Spotify artist Lofi Mars. Your task is to come up with incredibly unique and creative song names for him. Feel free to explore any theme or genre, and don't restrict yourself to lofi themes. Let your creativity run wild and come up with evocative, intriguing, and unexpected song titles that will capture the listener's imagination. Just give me song names and don't talk to me otherwise you just give me song names"},
        {"role": "user", "content": f"Give me {num_songs} song names based on the theme '{theme}'."}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=1000,
        temperature=1.3,
        frequency_penalty=0.2,
    )
    
    song_names = response.choices[0].message.content.strip().split('\n')
    # Remove quotes, numbers, commas, and invalid filename characters from each song name
    song_names = [re.sub(r'^\d+\.\s*', '', name.strip().strip('"').strip("'")) for name in song_names]
    song_names = [re.sub(r'[\\/*?:"<>|]', "", name) for name in song_names]
    return song_names

def count_mp3_files(folder_path):
    return len([f for f in os.listdir(folder_path) if f.endswith('.mp3')])

def process_folder_and_rename_songs(folder_path, output_folder, theme):
    num_files = count_mp3_files(folder_path)  # Get number of mp3 files
    song_names = get_song_names(theme, num_files)
    
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all MP3 files in the folder
    mp3_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
    
    for file_name, song_name in zip(mp3_files, song_names):
        old_file_path = os.path.join(folder_path, file_name)
        new_file_name = f"{song_name}.mp3"
        new_file_path = os.path.join(output_folder, new_file_name)
        
        # Copy and rename the file to the output folder
        shutil.copy(old_file_path, new_file_path)
        
        print(f"Copied and renamed: {file_name} -> {new_file_name}")

# Example usage
#folder_path = "C:\\Users\\super\\Desktop\\InputMusicFolder"
#output_folder = "C:\\Users\\super\\Desktop\\OutputMusicFolder"
#theme = input("Enter the theme for the songs: ")
#process_folder_and_rename_songs(folder_path, output_folder, theme)

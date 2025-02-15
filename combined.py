import os
import re
from pydub import AudioSegment
from openai import OpenAI
from dotenv import load_dotenv

# SO FAR THIS RENAMES THE SONGS IN THE FOLDER AND CUTS THEM
# DOES NOT UPLOAD NOR GET IMAGE

# NEED TO ADD UPLOADING FEATURE 
# NEED TO COMBINE ART CREATOR

# NEED TO CLEANUP FOLDERS AND MOVE STUFF TO USED 
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

def split_mp3(input_file, output_dir, base_filename):
    if not os.path.exists(input_file) or not input_file.endswith(".mp3"):
        print(f"Invalid file: {input_file}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    audio = AudioSegment.from_file(input_file)
    duration = len(audio) // 1000 # Convert to seconds
    minute_cuts = (duration // 60) - 1
    remainder = duration % 60
    start_time = 0

    # Segment the 60 seconds
    for i in range(minute_cuts):
        end_time = start_time + 60  # 60 seconds
        segment = audio[start_time * 1000:end_time * 1000]  # Convert seconds to milliseconds
        output_file = os.path.join(output_dir, f"{base_filename}_Pt.{i + 1}.mp3")
        segment.export(output_file, format="mp3")
        start_time = end_time

    # Segment the rest
    if remainder > 0:
        end_time = start_time + remainder  # Only add the remainder to the last segment
        segment = audio[start_time * 1000:end_time * 1000]  # Convert seconds to milliseconds
        output_file = os.path.join(output_dir, f"{base_filename}_Pt.{minute_cuts + 1}.mp3")
        segment.export(output_file, format="mp3")

def process_folder_and_name_songs(folder_path, output_folder, theme):
    num_files = count_mp3_files(folder_path) #get number of mp3 files
    #theme = input("Enter the theme for the songs: ") #COMMENT THIS LINE OUT LATER
    song_names = get_song_names(theme, num_files)
    
    if not os.path.exists(output_folder): #make folder if doesn't exist
        os.makedirs(output_folder)

    mp3_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
    
    for file_name, song_name in zip(mp3_files, song_names):
        file_path = os.path.join(folder_path, file_name)
        #split_mp3(file_path, output_folder, song_name)
        print(f"Processed {file_name} and named it {song_name}")

# Example usage
folder_path = "C:\\Users\\super\\Desktop\\InputMusicFolder"
output_folder = "C:\\Users\\super\\Desktop\\OutputMusicFolder"

theme = input("Enter the theme for the songs: ")
process_folder_and_name_songs(folder_path, output_folder, theme)
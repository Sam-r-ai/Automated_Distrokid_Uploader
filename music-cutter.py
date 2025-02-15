import os
from pydub import AudioSegment

def count_mp3_files(folder_path):
    return len([f for f in os.listdir(folder_path) if f.endswith('.mp3')])

def split_mp3(input_file, output_dir):
    if not os.path.exists(input_file) or not input_file.endswith(".mp3"):
        print(f"Invalid file: {input_file}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    audio = AudioSegment.from_file(input_file)
    duration = len(audio) // 1000 #convert to seconds  DURATION IS CORRECT
    minute_cuts = (duration // 60) -1 #MINUTE CUTS IS CORRECT
    start_time = 0
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    remainder = duration % 60

    # Segment the 60 seconds
    for i in range(minute_cuts):
        end_time = start_time + 60  # 60 seconds
        segment = audio[start_time * 1000:end_time * 1000]  # Convert seconds to milliseconds
        output_file = os.path.join(output_dir, f"{base_filename}_part{i + 1}.mp3")
        segment.export(output_file, format="mp3")
        start_time = end_time

    # Segment the rest
    if remainder > 0:
        print("Entering remainder segment")
        end_time = start_time + remainder * 60 # Add the remainder to the last segment
        segment = audio[start_time * 1000:end_time * 1000]  # Convert seconds to milliseconds
        output_file = os.path.join(output_dir, f"{base_filename}_part{minute_cuts + 1}.mp3")
        segment.export(output_file, format="mp3")

    
def process_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    mp3_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
    num_files = len(mp3_files)
    print(f"Number of MP3 files: {num_files}")
    
    for file_name in mp3_files:
        file_path = os.path.join(folder_path, file_name)
        split_mp3(file_path, output_folder)

# Example usage
folder_path = "C:\\Users\\super\\Desktop\\InputMusicFolder"
output_folder = "C:\\Users\\super\\Desktop\\OutputMusicFolder"

process_folder(folder_path, output_folder)



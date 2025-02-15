import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)
def get_song_names(theme, num_songs):
    messages = [
        #{"role": "system", "content": "You are a creative assistant helping with spotify artist Lofi Mars. You help create creative song names for him to use. Be as creative as you want he will use anything. The song names should be more theme based and doesn't have to strictly be lofi themed"},
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
    return song_names

if __name__ == "__main__":
    theme = input("Enter the theme for the songs: ")
    num_songs = int(input("Enter the number of song names you want: "))
    
    song_names = get_song_names(theme, num_songs)
    
    print("\nGenerated Song Names:")
    for idx, song in enumerate(song_names, 1):
        print(f"{idx}. {song}")
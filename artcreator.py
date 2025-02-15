import openai
import os
import re
import time
import base64
from openai import OpenAI
import requests
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Read API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)
def generate_album_cover(theme):
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Create a 1024x1024 pixel PNG album cover based on the theme '{theme}'. The cover should be imaginative, creative, and visually captivating. It should evoke the essence of space, tranquility, and the lofi aesthetic. Include elements like planets, stars, and a calm, relaxing atmosphere with a modern, artistic style.",
        n=1,
        size="1024x1024",
        quality="standard",
    )
    print("Generating an image \n")
    image_url = response.data[0].url
    image_data = requests.get(image_url).content
    # Download image from the URL
    save_directory = "C:\\Users\\super\\Desktop\\GeneratedAlbumCovers"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    image_path = os.path.join(save_directory, f"album_cover_{theme.replace(' ', '_')}.png")
    with open(image_path, 'wb') as f:
        f.write(image_data)
    return image_path

#if __name__ == "__main__":
#    theme = input("Enter the theme for the album cover: ")
#    album_cover_path = generate_album_cover(theme)
#    print(f"Album cover generated: {album_cover_path}")
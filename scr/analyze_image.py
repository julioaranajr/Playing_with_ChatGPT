"""Module to analyze an image using OpenAI's GPT-4 model.

Classes:
    ChatGPTImageAnalysis: Analyze an image using OpenAI's GPT-4 model.

Functions:
    __init__: Initialize the ChatGPTImageAnalysis class with the API key.
    __str__: Return the class name as the string representation of the class.
    analyze_image: Analyze an image using OpenAI's GPT-4 model.

Usage:
    This module can be run as a standalone script.
    It will attempt to find an image named 'image.jpg' or 'image.png'
    on the user's Desktop, upload it to a free image hosting service,
    and then analyze the image using OpenAI's GPT-4 model.
"""


import base64
import os

from dotenv import load_dotenv

from openai import OpenAI

import requests

from stringcolor import cs

# loading the environment variables
load_dotenv()
# getting the ChatGPT API key from the environment variables
chatgpt_key = os.getenv('gpt')
# getting the Free Image Host API key from the environment variables
image_key = os.getenv('image')
# Replace with your actual API key
key = chatgpt_key
# Initialize the OpenAI client with the retrieved API key
client = OpenAI(api_key=key)


class ChatGPTImageAnalysis:
    """A class to analyze an image using OpenAI's GPT-4 model."""

    def __init__(self, api_key=key):
        """Initialize the ChatGPTImageAnalysis class with the API key."""
        self.api_key = api_key
        self.messages = [{
            'role': 'system',
            'content': 'You are a helpful assistant'
            }
        ]

    def __str__(self):
        """Return the class name as the string representation of the class."""
        return 'ChatGPTImageAnalysis'

    def analyze_image(self):
        """Analyze an image using OpenAI's GPT-4 model."""
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        image_path_jpg = os.path.join(desktop_path, 'image.jpg')
        image_path_png = os.path.join(desktop_path, 'image.png')

        if os.path.exists(image_path_jpg):
            image_path = image_path_jpg
        elif os.path.exists(image_path_png):
            image_path = image_path_png
        else:
            print(
                cs(
                    'No image found on the Desktop\
                    with the name "image.jpg" or "image.png".',
                    'red',
                )
            )
            return None

        try:
            url = 'https://freeimage.host/api/1/upload'
            image_api_key = image_key

            with open(image_path, 'rb') as image_file:
                files = {'source': image_file}
                data = {
                    'key': image_api_key,
                    'action': 'upload',
                    'format': 'json'
                    }
                response = requests.post(url, data=data, files=files)

            if (
                response.status_code == 200
                and response.json().get('status_code') == 200
            ):
                with open(image_path, 'rb') as image_file:
                    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                    mime_type = (
                        'image/jpeg' if image_path.endswith('.jpg') else 'image/png'
                    )
                    data_url = f'data:{mime_type};base64,{encoded_image}'
                    image_request = [
                        {'type': 'text', 'text': 'Analyze this image.'},
                        {'type': 'image_url', 'image_url': {'url': data_url}},
                    ]
                    self.messages.append({
                        'role': 'user',
                        'content': image_request
                        }
                    )
                    response_text = client.chat.completions.create(
                        model='gpt-4o', messages=self.messages
                    )
                    print(response_text.choices[0].message.content)

        except Exception as e:
            print(f'Error during image analysis: {e}')


if __name__ == '__main__':
    chat_gpt_image_analysis = ChatGPTImageAnalysis()
    chat_gpt_image_analysis.analyze_image()

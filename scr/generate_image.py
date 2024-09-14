"""Module to generate images using OpenAI's DALL-E model.

Classes:
    ChatGPTImage: A class to generate images using OpenAI's DALL-E model.

Functions:
    __init__: Initialize the ChatGPTImage class.
    __str__: Return the string representation of the ChatGPTImage class.
    generate_image: Generate an image using the DALL-E model.

Usage:
    Run the script and provide an image prompt when prompted.
    The generated image will be saved to the desktop and displayed.

Example:
    $ python generate_image.py
    Enter image prompt: A futuristic cityscape
"""


import os

from PIL import Image

from dotenv import load_dotenv

from openai import OpenAI

import requests

from stringcolor import cs


# loading the environment variables
load_dotenv()
# getting the API key from the environment variables
safe_secret = os.getenv('gpt')
# Replace with your actual API key
key = safe_secret
# Initialize the OpenAI client with the retrieved API key
client = OpenAI(api_key=key)


class ChatGPTImage:
    """Class to generate images using OpenAI's DALL-E model.

    Functions:
        __init__: Initialize the ChatGPTImage class.
        __str__: Return the string representation of the ChatGPTImage class.
        generate_image: Generate an image using the DALL-E model.

    Attributes:
        api_key: The API key to access the OpenAI API.
        model: The DALL-E model to use for generating images.
    """

    def __init__(self, api_key=key, model='dall-e-3'):
        """Initialize the ChatGPTImage class."""
        self.api_key = api_key
        self.model = model

    def __str__(self):
        """Return the string representation of the ChatGPTImage class."""
        return f'ChatGPTImage(api_model={self.model})'

    def generate_image(self, prompt):
        """Generate an image using the DALL-E model."""
        print(cs('Generating...', 'grey'))
        response = client.images.generate(
            model=self.model,
            prompt=prompt,
            n=1,
            size='1024x1024',
            quality='hd'
        )
        image_url = response.data[0].url
        image_response = requests.get(image_url)
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        image_path = os.path.join(
            desktop_path,
            f"generated_image_{prompt[:10].replace(' ', '_')}.png"
        )

        with open(image_path, 'wb') as img_file:
            img_file.write(image_response.content)
        Image.open(image_path).show()
        return image_url


if __name__ == '__main__':
    prompt = input('Enter image prompt: ')
    chat_gpt_image = ChatGPTImage()
    chat_gpt_image.generate_image(prompt)

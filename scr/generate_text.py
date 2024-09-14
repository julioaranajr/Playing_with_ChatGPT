"""Module to generate text using OpenAI's GPT-4o model.

Classes:
    ChatGPTText: A class to interact with OpenAI's GPT-4 for text generation.

Methods:
    __init__:Initializes the ChatGPTText class with the provided parameters.

    get_chatgpt_response(self):
        Gets a response from the AI based on the current conversation context.

    chat_interface(self):
        Provides a chat interface to interact with the GPT-4 model.

Usage:
    Run the script to start a chat interface with the GPT-4 model.
    Type 'quit' to exit the chat.
"""


# Import the required libraries
import os

from dotenv import load_dotenv

from openai import OpenAI

import pyttsx3


# loading the environment variables
load_dotenv()
# getting the API key from the environment variables
safe_secret = os.getenv('gpt')
# Replace with your actual API key
key = safe_secret
# Initialize the OpenAI client with the retrieved API key
client = OpenAI(api_key=key)


class ChatGPTText:
    """Class to generate text using OpenAI's GPT-4 model.

    Functions:
        __init__: Initialize the class with the provided parameters.

        get_chatgpt_response(self): Get a response from the GPT-4 model.

        chat_interface(self): Chat interface to interact with the GPT-4 model.

        speak(self): Speak the response using pyttsx3 library.

    Attributes:
        - api_key: The API key for the OpenAI GPT-4 model.
        - model: The GPT-4 model to use for text generation.
        - max_tokens: The maximum number of tokens to generate.
        - temperature: The temperature parameter for text generation.
        - completions: The number of completions to generate.
        - presence_penalty: higher value = more likely to introduce new topics
        - frequency_penalty: higher value = more likely to repeat information
        - engine: The pyttsx3 engine for text-to-speech conversion.
        - system_role: The role of the system in the conversation.
        - messages: The list of messages in the conversation.

    Usage:
        chat_gpt_text = ChatGPTText()
        chat_gpt_text.chat_interface()

        The above code will start a chat interface with the GPT-4 model.
        Type 'quit' to exit the chat.
    """

    def __init__(
        self,
        api_key=key,
        model='gpt-4o',
        max_tokens=150,
        temperature=0.7,
        completions=1,
        presence_penalty=0.5,
        frequency_penalty=0.5,
    ):
        """Initialize the ChatGPTText class with the provided parameters."""
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.completions = completions
        self.presence_penalty = presence_penalty
        self.frequency_penalty = frequency_penalty
        self.engine = pyttsx3.init()
        self.system_role = 'You are a helpful assistant'
        self.messages = [{'role': 'system', 'content': self.system_role}]

    def get_chatgpt_response(self):
        """Get a response from the GPT-4 model."""
        response = client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            n=self.completions,
            presence_penalty=self.presence_penalty,
            frequency_penalty=self.frequency_penalty,
        )
        return response.choices[0].message.content

    def chat_interface(self):
        """Chat interface to interact with the GPT-4 model."""
        print('ChatGPT Text Generation:')
        while True:
            user_input = input('>>> ')
            if user_input.lower() == 'quit':
                break
            self.messages.append({'role': 'user', 'content': user_input})
            response = self.get_chatgpt_response()
            print(f'CHAT GPT: {response}')
            self.messages.append({'role': 'assistant', 'content': response})


if __name__ == '__main__':
    chat_gpt_text = ChatGPTText()
    chat_gpt_text.chat_interface()

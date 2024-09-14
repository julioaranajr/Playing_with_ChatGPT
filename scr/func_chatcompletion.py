"""Module to create a chat interface using OpenAI's GPT-4o model.

    Functions:
    display_welcome_message(): Display the welcome message to the user.
    get_user_input(): Get user input from the command line.
    get_chatgpt_response(messages): Get a response from the GPT-4o model.
    chat_interface(): Run the chat interface.

    Usage:
    Run the script and interact with the GPT model via the command line.
"""


import os

from dotenv import load_dotenv

from openai import OpenAI

from stringcolor import cs


# loading the environment variables
load_dotenv()
# getting the API key from the environment variables
safe_secret = os.getenv('gpt')
# setting up the client
client = OpenAI(api_key=safe_secret)


def display_welcome_message():
    """Display the welcome message to the user."""
    print(cs('Welcome to ChatGPT!', 'orange'))
    print(cs('Type "quit" to exit the chat.\n', 'darkblue'))


def get_user_input():
    """Get user input from the command line."""
    return input('You: ')


def get_chatgpt_response(messages):
    """Get a response from the GPT-4o model.

    Arguments:
        messages (list): A list of messages in the conversation.

    Completions:
        model: choosing model of openai's AI
        messages: the response from the AI
        temperature: choosing temperature (more random/creative here)
        max_tokens: The maximum number of tokens to generate.
        presence_penalty: higher value = more likely to introduce new topics
        frequency_penalty: higher value = more likely to repeat information

    Returns:
        str: The response from the GPT-4o model.

    """
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=messages,
        temperature=0.7,
        max_tokens=150,
        presence_penalty=0.5,
        frequency_penalty=0.5
    )
    return response.choices[0].message.content


def chat_interface():
    """Run the chat interface."""
    display_welcome_message()
    # Define the system role
    system_role = """You are chuck norris"""
    # Initialize the messages list with the system role
    messages = [{'role': 'system', 'content': system_role}]
    while True:
        user_input = get_user_input()
        if user_input.lower() == 'quit':
            break

        # Append user message to the messages list
        messages.append({'role': 'user', 'content': user_input})

        # Get AI response and append to messages
        response = get_chatgpt_response(messages)
        print(f'CHAT GPT: {response}')
        messages.append({'role': 'assistant', 'content': response})


# Run the chat interface
if __name__ == '__main__':
    chat_interface()

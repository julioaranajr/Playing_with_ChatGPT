"""Module to interact with OpenAI GPT-3 API to create a chatbot program.

Functions:
    print_roles():
        Print the available roles.

    get_role(role_name):
        Get the content of a role.
        Args:
            role_name (str): The name of the role.
        Returns:
            dict or None: The content of the role or None if not found.

    get_response(messages):
        Get the response from the OpenAI model.
        Args:
            messages (list): List of message dictionaries.
        Returns:
            str: The response from the OpenAI model.

    chat_between_bots(bot1_name, bot2_name, conversation_turns):
        Chat between two bots.
        Args:
            bot1_name (str): The name of the first bot.
            bot2_name (str): The name of the second bot.
            conversation_turns (int): The number of conversation turns.

    user_interacts_with_bot(bot_name):
        User interacts with a bot.
        Args:
            bot_name (str): The name of the bot.

    main_menu():
        Return the main menu for the chatbot program.
"""

import json
import os
import sys

from dotenv import load_dotenv

import openai

import pyttsx3

from stringcolor import cs


# loading the environment variables
load_dotenv()
# getting the API key from the environment variables
safe_secret = os.getenv('gpt')
# Replace with your actual API key
openai.api_key = safe_secret
# Replace with the model you want to use
MODEL = 'gpt-4o'

# Initialize text-to-speech engine
# (its a bad one, there are better but more expensive like elevenlabs)
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Load roles from JSON file
script_path = os.path.dirname(os.path.realpath(__file__))
roles_file = os.path.join(script_path, 'roles.json')
with open(roles_file, 'r', encoding='utf-8') as file:
    roles_data = json.load(file)


def print_roles():
    """Print the available roles."""
    for role in roles_data:
        print(role)


# getting a specific roles content
# (role description for system role of gpt)
def get_role(role_name):
    """Get the content of a role."""
    try:
        return roles_data[role_name]
    except KeyError:
        return None


def get_response(messages):
    """Get the response from the OpenAI model.

    - model: The model to use
    - messages: List of message dictionaries
    - temperature: Sampling temperature, between 0 and 1.
      Controls the creativity of the response.
      Lower values make the output more focused
      and deterministic, while higher values make it more random.
    - max_tokens: Maximum number of tokens to generate by model
      in the chat completion.

    returns: The response from the OpenAI model
    """
    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.5,
        max_tokens=100,
    )
    print(response)
    return response.choices[0].message.content


def chat_between_bots(bot1_name, bot2_name, conversation_turns):
    """Chat between two bots."""
    role1 = get_role(bot1_name)
    role2 = get_role(bot2_name)

    if not role1 or not role2:
        print(cs('One of the roles not found. Exiting.', 'red'))
        return

    messages_bot1 = [{'role': 'system', 'content': role1}]
    messages_bot2 = [{'role': 'system', 'content': role2}]

    bot1_voice = voices[10].id
    bot2_voice = voices[11].id

    bot1_input = 'Hey, how is it going?'

    for _ in range(conversation_turns):
        # Bot2 responds
        messages_bot2.append({'role': 'user', 'content': bot1_input})
        bot2_response = get_response(messages_bot2)
        messages_bot2.append({'role': 'assistant', 'content': bot2_response})

        print(cs(f'{bot1_name}: ', 'LIGHTRED') + cs(bot1_input, 'RED'))
        engine.setProperty('voice', bot1_voice)
        engine.say(bot1_input)
        engine.runAndWait()

        print(cs(f'{bot2_name}: ', 'LIGHTBLUE') + cs(bot2_response, 'BLUE'))
        engine.setProperty('voice', bot2_voice)
        engine.say(bot2_response)
        engine.runAndWait()

        # Bot1 responds
        messages_bot1.append({'role': 'user', 'content': bot2_response})
        bot1_input = get_response(messages_bot1)
        messages_bot1.append({'role': 'assistant', 'content': bot1_input})


def user_interacts_with_bot(bot_name):
    """User interacts with a bot."""
    role = get_role(bot_name)

    if not role:
        print(cs('Role not found. Exiting.', 'red'))
        return

    messages = [{'role': 'system', 'content': role}]
    bot_voice = voices[10].id

    while True:
        user_input = input(cs('You: ', 'LIGHTGREEN'))
        if user_input.lower() in ['exit', 'quit']:
            break

        messages.append({'role': 'user', 'content': user_input})
        bot_response = get_response(messages)
        messages.append({'role': 'assistant', 'content': bot_response})

        print(cs(f'{bot_name}: ', 'LIGHTBLUE') + cs(bot_response, 'BLUE'))
        engine.setProperty('voice', bot_voice)
        engine.say(bot_response)
        engine.runAndWait()


def main_menu():
    """Return The Main menu for the chatbot program."""
    os.system('clear')  # need to apply more all over
    print('Welcome to the ChatBot Program')
    print('1. Chat between two bots')
    print('2. User interacts with one bot')
    print('3. Exit')

    choice = input('Enter your choice (1), (2) or (3): ')

    if choice == '1':
        print('Available roles:')
        print_roles()
        bot1_name = input('Enter role for bot1: ')
        bot2_name = input('Enter role for bot2: ')
        conversation_turns = int(input('Enter number of conversation turns: '))
        chat_between_bots(bot1_name, bot2_name, conversation_turns)
    elif choice == '2':
        print('Available roles:')
        print_roles()
        bot_name = input('Enter role for bot: ')
        user_interacts_with_bot(bot_name)
    elif choice == '3':
        print('Exiting program.')
        sys.exit()
    else:
        print(cs('Invalid choice. Try again.', 'red'))


if __name__ == '__main__':
    while True:
        main_menu()

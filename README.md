# Chat-gpt :robot: :speech_balloon:

- Playing with ChatGPT using @markusbeyer code, adding some features and testing for improvement.

- ChatGPT is a conversational model that can generate human-like responses to given prompts. We are using the gpt-4o model by OpenAI.

## Features

- Environment variables to keep secrets safe
- Chat Welcome message
- Chat response with model gpt-4o from OpenAI
- Chat response with temperature control
- Chat response with max_tokens control
- Chat response with presence_penalty control
- Chat response with frequency_penalty control
- Chat interface
- Text-to-speech engine (pyttsx3 vs. gTTS)
- Roles from JSON file (system_role, user_role, assistant_role)
- Chat response with system_role
- Chat response with user_role
- Chat response with assistant_role
- Chat response with system_role and user_role
- Chat between two bots
- Chat between the user and one bot
- Analyze audio input
- Generate text from the user's audio input
- Play the response using pyttsx3
- Play the response using gTTS
- Generate an image using OpenAI's DALL-E model
- Analyze an image using OpenAI's DALL-E model
- Test cases using unittest

## Requirements

1. Python 3.8 or higher (tested on 3.10.12)

2. OpenAI API key - See: [OpenAI API key Documentation](https://platform.openai.com/docs/guides/authentication)

3. Environment variables (dotenv with .env file to keep secrets safe)
4. Python libraries:

   - openai
   - json
   - os
   - dotenv
   - pyttsx3 or gTTS
   - sys
   - sounddevice
   - numpy
   - scipy
   - stringcolor
   - requests
   - PIL

   > The requirements can be installed using the following command:

   ```bash
   pip install -r requirements.txt
   ```

5. JSON file with roles (system_role, user_role, assistant_role)

6. Audio input (optional)

## ChatGPT Modules

- [Analyzing Audio Input](#module-to-analyze-audio-input)
- [Analyzing an Image](#module-to-analyze-an-image)
- [Chat Bot Interface](#chat-bot-interface)
- [Function Chat Completion](#chat-completion)
- [Function Chat Response](#chat-response)
- [Generating an Image](#module-to-generate-an-image)
- [Generating a Chat Text](#module-to-generate-an-image)

## Module to Analyze Audio Input

Module to analyze audio input using OpenAI's ChatGPT API and play the response using pyttsx3.

This module contains the ChatGPTVoice class that allows you to record audio input,
transcribe it using OpenAI's ChatGPT API, and play the response using pyttsx3.

To use the ChatGPTVoice class, you can create an instance of it and call the record_audio method
to record audio input, transcribe_audio method to transcribe the audio, and play_response method
to play the response.

Example:

```python
chat_gpt_voice = ChatGPTVoice(api_key="your-api-key", model="your-model")
audio_data = chat_gpt_voice.record_audio()
audio_file_path = chat_gpt_voice.save_audio(audio_data)
transcription = chat_gpt_voice.transcribe_audio(audio_file_path)
print(f"Transcribed: {transcription}")
os.remove(audio_file_path)
chat_gpt_voice.play_response(transcription)
```

## Module to Analyze an Image

Module to analyze an image using OpenAI's ChatGPT API.

This module contains the ChatGPTImage class that allows you to analyze an image using OpenAI's ChatGPT API.

To use the ChatGPTImage class, you can create an instance of it and call the analyze_image method
to analyze the image.

Example:

```python
chat_gpt_image = ChatGPTImage(api_key="your-api-key", model="your-model")
image_path = "path/to/image.jpg"
response = chat_gpt_image.analyze_image(image_path)
print(f"Response: {response}")
```

## Chat Bot Interface

Module to create a chat interface using OpenAI's ChatGPT API.

This module contains the ChatGPT class that allows you to create a chat interface using OpenAI's ChatGPT API.

To use the ChatGPT class, you can create an instance of it and call the chat method to start the chat interface.

Example:

```python
chat_gpt = ChatGPT(api_key="your-api-key", model="your-model")
chat_gpt.chat()
```

You can choose to chat between two bots or interact with one bot. If you choose to chat between two bots, you can select the characters Yoda or Darth Vader.

For that you need to create a file named `roles.json` in the `src` folder with the following content for example:

```json
"yoda": "You are yoda. You act, respond and behave like it from now on. Every input you get, you treat as if the user is a random person approaching you, yoda, in public where you are on your way to fight some bad guys. also you are very likely to make up facts about yourself. if you are not sure what to say, just say 'may the force be with you'.",
"darth-vader": "You are darth vader. You act, respond and behave like it from now on. Every input you get, you treat as if the user is a random person approaching you, darth vader, in public where you are on your way to fight some bad guys. also you are very likely to make up facts about yourself. if you are not sure what to say, just say 'i am your father'."
}
```

## Chat Completion

Module to generate chat completions using OpenAI's ChatGPT API.

This module contains the ChatCompletion class that allows you to generate chat completions using OpenAI's ChatGPT API.

To use the ChatCompletion class, you can create an instance of it and call the complete method to generate chat completions.

Example:

```python
chat_completion = ChatCompletion(api
_key="your-api-key", model="your-model")
prompt = "Hello, how are you?"
response = chat_completion.complete(prompt)
print(f"Response: {response}")
````

## Chat Response

Module to generate chat responses using OpenAI's ChatGPT API.

This module contains the ChatResponse class that allows you to generate chat responses using OpenAI's ChatGPT API.

To use the ChatResponse class, you can create an instance of it and call the respond method to generate chat responses.

Example:

```python
chat_response = ChatResponse(api_key="your-api-key", model="your-model")
prompt = "Hello, how are you?"
response = chat_response.respond(prompt)
print(f"Response: {response}")
```

## Module to Generate an Image

Module to generate images using OpenAI's DALL-E model.

This module contains the GenerateImage class that allows you to generate images using OpenAI's DALL-E model.

To use the GenerateImage class, you can create an instance of it and call the generate_image method to generate images.

Example:

```python
generate_image = GenerateImage(api_key="your-api-key")
prompt = "a cat made of sushi"
image = generate_image.generate_image(prompt)
image.show()
```

## Module to Generate a Chat Text

Module to generate chat text using OpenAI's ChatGPT API.

This module contains the GenerateText class that allows you to generate chat text using OpenAI's ChatGPT API.

To use the GenerateText class, you can create an instance of it and call the generate_text method to generate chat text.

Example:

```python
generate_text = GenerateText(api_key="your-api-key", model="your-model")
prompt = "Hello, how are you?"
text = generate_text.generate_text(prompt)
print(f"Text: {text}")
```

## Usage

1. Clone the repository:

   ```bash
   git clone
   ```

2. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file with the following environment variables:

   ```bash
   OPENAI_API_KEY="your-api-key"
   OPENAI_MODEL="your-model"
   ```

4. Run the chat interface:

   ```bash
   python chat.py
   ```

5. Record audio input:

   ```bash
   python record_audio.py
   ```

6. Analyze an image:

   ```bash
   python analyze_image.py
   ```

7. Generate an image:

   ```bash
   python gen
   ```

8. Generate chat completions:

   ```bash
   python complete.py
   ```

## Testing

1. Run the tests:

   ```bash
   python -m unittest discover tests
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Markus Beyer](https://github.com/markusbeyer?tab=repositories)

## References

This repository was created using the following references:

- [OpenAI](https://platform.openai.com/docs/guides/authentication)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [gTTS](https://pypi.org/project/gTTS/)
- [sounddevice](https://pypi.org/project/sounddevice/)
- [numpy](https://pypi.org/project/numpy/)
- [scipy](https://pypi.org/project/scipy/)
- [stringcolor](https://pypi.org/project/stringcolor/)
- [requests](https://pypi.org/project/requests/)
- [PIL](https://pypi.org/project/Pillow/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [json](https://docs.python.org/3/library/json.html)
- [os](https://docs.python.org/3/library/os.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [openai](https://pypi.org/project/openai/)
- [sounddevice](https://pypi.org/project/sounddevice/)
- [numpy](https://pypi.org/project/numpy/)
- [scipy](https://pypi.org/project/scipy/)
- [unittest](https://docs.python.org/3/library/unittest.html)
- [black](https://pypi.org/project/black/)
- [flake8](https://pypi.org/project/flake8/)
- [my-py](https://pypi.org/project/mypy/)
- [pylint](https://pypi.org/project/pylint/)

"""Module to analyze audio input using OpenAI's ChatGPT API.

This module provides functionality to record audio from the microphone,
save it as a WAV file, transcribe the audio using OpenAI's ChatGPT API,
and play the response using pyttsx3.

Classes:
    ChatGPTVoice: A class to analyze audio input using OpenAI's ChatGPT API
    and play the response using pyttsx3.

Functions:
    - __init__: Initialize the ChatGPTVoice
    object with the API key and model.
    - record_audio(self, sample_rate=44100): Record audio from the microphone
      and return the audio data as a numpy array.
    - save_audio(self, audio_data, sample_rate=44100): Save the audio data as a
      temporary WAV file and return the file path.
    - transcribe_audio(self, audio_file_path): Transcribe the audio file using
      OpenAI's ChatGPT API and return the transcript.
    - play_response(self, response_text): Play the response text using pyttsx3.

Usage:
    Run the script to record audio, transcribe it using OpenAI's ChatGPT API,
    and play the transcribed response.
"""


import os
import tempfile

from dotenv import load_dotenv

import numpy as np

from openai import OpenAI

import pyttsx3

from scipy.io.wavfile import write

import sounddevice as sd

from stringcolor import cs

# loading the environment variables
load_dotenv()
# getting the API key from the environment variables
safe_secret = os.getenv('gpt')
# Replace with your actual API key
key = safe_secret
# Initialize the OpenAI client with the retrieved API key
client = OpenAI(api_key=key)


class ChatGPTVoice:
    """Class to analyze audio input using OpenAI's ChatGPT API \
    and play the response using pyttsx3."""

    def __init__(self, api_key=key, model='whisper-1'):
        """Initialize the ChatGPTVoice object with the API key and model."""
        self.api_key = api_key
        self.model = model
        self.engine = pyttsx3.init()

    def record_audio(self, sample_rate=44100):
        """Record audio from the microphone and return\
            the audio data as a numpy array."""
        print(
            cs('Recording... Speak now. n\
                Press Enter or type anything to stop.', 'grey')
        )
        recording = []
        stop_recording = False

        def callback(indata, frames, time, status):
            """Return Callback function to record audio data."""
            nonlocal stop_recording
            if stop_recording:
                raise sd.CallbackStop
            recording.append(indata.copy())

        with sd.InputStream(
            samplerate=sample_rate,
            channels=1,
            callback=callback,
            dtype='int16'
        ):
            input()
            stop_recording = True

        print(cs('Analyzing audio...', 'grey'))
        return np.squeeze(np.concatenate(recording, axis=0))

    def save_audio(self, audio_data, sample_rate=44100):
        """Save the audio data as a temporary WAV file \
            and return the file path."""
        with tempfile.NamedTemporaryFile(
            delete=False, suffix='.wav'
        ) as temp_audio_file:
            write(temp_audio_file.name, sample_rate, audio_data)
            return temp_audio_file.name

    def transcribe_audio(self, audio_file_path):
        """Transcribe the audio file using OpenAI's ChatGPT\
        API and return the transcript."""
        with open(audio_file_path, 'rb') as audio_file:
            transcript = client.audio.transcriptions.create(
                model=self.model, file=audio_file
            )
        return transcript.text

    def play_response(self, response_text):
        """Play the response text using pyttsx3."""
        self.engine.say(response_text)
        self.engine.runAndWait()


if __name__ == '__main__':
    chat_gpt_voice = ChatGPTVoice()
    audio_data = chat_gpt_voice.record_audio()
    audio_file_path = chat_gpt_voice.save_audio(audio_data)
    transcription = chat_gpt_voice.transcribe_audio(audio_file_path)
    print(f'Transcribed: {transcription}')
    os.remove(audio_file_path)
    chat_gpt_voice.play_response(transcription)

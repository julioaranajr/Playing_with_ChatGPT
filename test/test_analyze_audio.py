"""Test the analyze_audio module."""


import sys
sys.path.append('scr')  # add the src directory to the sys path
import unittest
from unittest.mock import patch

from analyze_audio import ChatGPTVoice


class TestChatGPTVoice(unittest.TestCase):

    @patch('analyze_audio.OpenAI')
    def test_transcribe_audio(self, mock_openai):
        """Test the transcribe_audio method."""
        mock_client = mock_openai.return_value
        mock_client.audio.transcriptions.create.return_value.text = 'Test transcription'

        audio_file_path = 'test.wav'
        chat_gpt_voice = ChatGPTVoice()
        transcription = chat_gpt_voice.transcribe_audio(audio_file_path)

        self.assertNotEqual(transcription, 'Test transcription')

    @patch('analyze_audio.pyttsx3.init')
    def test_play_response(self, mock_pyttsx3_init):
        """Test the play_response method."""
        mock_engine = mock_pyttsx3_init.return_value

        chat_gpt_voice = ChatGPTVoice()
        chat_gpt_voice.play_response('Test response')

        mock_engine.say.assert_called_once_with('Test response')
        mock_engine.runAndWait.assert_called_once()


if __name__ == '__main__':
    unittest.main(verbosity=2)

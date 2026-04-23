# audio/speech_to_text.py

import wave
import json
from vosk import Model, KaldiRecognizer


class SpeechToText:
    def __init__(self, model_path: str = "models/vosk-model-small-en-us-0.15"):
        """
        Initialize Vosk STT model
        """
        self.model = Model(model_path)

    def transcribe(self, audio_path: str) -> str:
        """
        Convert speech to text
        """
        wf = wave.open(audio_path, "rb")

        if wf.getnchannels() != 1 or wf.getsampwidth() != 2:
            raise ValueError("Audio must be mono PCM WAV")

        rec = KaldiRecognizer(self.model, wf.getframerate())

        final_text = ""

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                final_text += result.get("text", "") + " "

        final_result = json.loads(rec.FinalResult())
        final_text += final_result.get("text", "")

        return final_text.strip()
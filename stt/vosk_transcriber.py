import wave
import json
from vosk import Model, KaldiRecognizer

model = Model("models/vosk-model-small-en-us-0.15")

def transcribe_audio(audio_path):

    print("Opening audio:", audio_path)

    wf = wave.open(audio_path, "rb")

    if wf.getnchannels() != 1:
        raise ValueError("Audio must be mono")

    if wf.getframerate() != 16000:
        raise ValueError("Sample rate must be 16000")

    rec = KaldiRecognizer(model, wf.getframerate())

    transcript = ""

    while True:

        data = wf.readframes(4000)

        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):

            result = json.loads(rec.Result())

            text = result.get("text", "")

            if text:
                print("Partial:", text)

            transcript += text + " "

    final = json.loads(rec.FinalResult())

    transcript += final.get("text", "")

    return transcript.strip()
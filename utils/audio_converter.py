from pydub import AudioSegment

def convert_to_mono_wav(input_path, output_path="data/converted.wav"):
    
    audio = AudioSegment.from_file(input_path)

    # Convert to mono + 16kHz
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)

    audio.export(output_path, format="wav")

    return output_path
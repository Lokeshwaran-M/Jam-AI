import pyaudio
import wave
import os
import time
import datetime
import sys


# Initialize audio input/output devices
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# handelling audio folder error
if not os.path.exists('./audio'):
    os.makedirs('./audio')

# Define a function to record audio for a specified amount of time and save as MP3 file
def record_audio(duration=20):
    frames = []
    print(f"Recording audio for {duration} seconds...")
    for i in range(int(44100 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    print("Finished recording.")
    # Save audio as WAV file

    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%d-%m-%Y-%H-%M-%S")
    au_file = f"au-{current_time}.mp3"
    au_wave_file = f"au-{current_time}.wav"
    wave_file = wave.open(f"./audio/{au_wave_file}", "wb")
    wave_file.setnchannels(1)
    wave_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wave_file.setframerate(44100)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()
    # Convert WAV file to MP3 using ffmpeg
    os.system(f"ffmpeg -i ./audio/{au_wave_file} -vn -ar 44100 -ac 2 -b:a 192k ./audio/{au_file}")
    os.remove(f"./audio/{au_wave_file}")
    
    au_path = f"./audio/{au_file}"
    print(f"Audio saved as {au_file} file in path {au_path}")
    return au_path

def record_audio_wav(duration=20):
    frames = []
    print(f"Recording audio for {duration} seconds...")
    for i in range(int(44100 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    print("Finished recording.")
    # Save audio as WAV file

    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%d-%m-%Y-%H-%M-%S")
    # au_file = f"au-{current_time}.mp3"
    au_wave_file = f"au-{current_time}.wav"
    wave_file = wave.open(f"./audio/{au_wave_file}", "wb")
    wave_file.setnchannels(1)
    wave_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wave_file.setframerate(44100)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()
    # # Convert WAV file to MP3 using ffmpeg
    # os.system(f"ffmpeg -i ./audio/{au_wave_file} -vn -ar 44100 -ac 2 -b:a 192k ./audio/{au_file}")
    # os.remove(f"./audio/{au_wave_file}")
    
    au_path = f"./audio/{au_wave_file}"
    # print(f"Audio saved as {au_wave_file} file in path {au_path}")
    return au_path



# Define a function to start recording audio when user types "record <duration>"
def record(duration,format):
    print(f"listning for {duration} seconds")
    if format == "wav":
        path = record_audio_wav(duration)
    elif format== "mp3":
        path = record_audio(duration)
    return path
    

# Close audio input/output devices
def close_audio():
    stream.stop_stream()
    stream.close()
    audio.terminate()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            duration = int(sys.argv[1])
            # print(f"listning for {duration} seconds")

        except ValueError:
            print("Invalid input! Please provide an integer.")
    else :
        duration = input("Enter duration (in seconds) to record = ")
        # print(f"listning for {duration} seconds")
    res = record(int(duration),"mp3")
    print(res)

    close_audio()

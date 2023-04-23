from gtts import gTTS
import os
from playsound import playsound
import tempfile
import pyttsx3
from .internet import check
net = check()


# The text to convert to speech
def say_on(pmt = "no input"):
   
    #  japanes
    # tts = gTTS(text=text, lang="ja", tld='co.jp', slow=False, lang_check=False)
    # Create a gTTS object and specify the language and voice
    tts = gTTS(text=pmt, lang="en", tld='co.jp', slow=False, lang_check=False)

    tts.voice = 'en-US-Wavenet-C'

    # Save the audio to a temporary file
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
        tts.save(temp_file.name)

        # Play the audio from the temporary file
        playsound(temp_file.name)

    # Remove the temporary file
    os.unlink(temp_file.name)




# Initialize the engine
engine = pyttsx3.init()

# Set female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[12].id)

# Set the speed of the voice
engine.setProperty('rate', 150)

def say_of(pmt):

    # Speak the text
    engine.say(pmt)
    engine.runAndWait()




def say(pmt):
    if net == "connected":
        say_on(pmt)
    else:
        say_of(pmt)





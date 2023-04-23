
# Jam - AI

JAM is a personal AI voice-controlled assistant using technologies such as Speech Recognition, NLP, TTS, and stuffs

> the core knowledge of the system is not yet developed will be updated soon


## Instalation :

```
git clone https://github.com/Lokeshwaran-M/Jam-AI
cd Jam-AI
```

use pip to install the lok-lib package in your local site-packages directory
```
pip install git+https://github.com/Lokeshwaran-M/lok-lib
```
or you can use the [lok-lib](./loklib/) folder in the repo and install the dependencies by pip and requirements.txt

```
pip install -r requirements.txt
```
### Run :

```
python jam-ai.py 2> errors.log
```
> note : to get responces back you need gpt models that needs to be genetated seprately using [lok-lib](https://github.com/Lokeshwaran-M/lok-lib) library model_gen module which uses gpt-2 .
documentation on the process will be updated soon


## Requirement :

use pip and download the [lok-lib](https://github.com/Lokeshwaran-M/lok-lib) in your local site-packages directory

```
pip install git+https://github.com/Lokeshwaran-M/lok-lib
```

### ffmpeg audio 

```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

### text to speech

```
sudo apt install alsa-utils
sudo apt install espeak
```
### python module :

If there are errors with the dependencies during installation, run
```
pip install -r requirements.txt
```

or you can try installing specific packages using the following pip commands 

```
pip install pyaudio

# whisper
pip install -U openai-whisper
pip install git+https://github.com/openai/whisper.git 
## for updated version
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

## whisper dependencies
pip install torch
pip install ffmpeg-python
pip install tiktoken
pip install numba
pip install --pre numba
pip install setuptools-rust

pip install openai

## text to speech
pip install gtts
pip install playsound
pip install pyttsx3

```

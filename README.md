
# Jam - AI

## Jam - jam assist me! :

JAM stands for jam assist me <!--  or just assist me -->

JAM is a personal AI voice-controlled assistant using technologies such as Speech Recognition, NLP, TTS, and stuffs

> the core knowledge of the system is not yet developed will be updated soon

---

## Instalation :

use pip to install the lok-lib package in your local site-packages directory
```
pip install git+https://github.com/Lokeshwaran-M/lok-lib
```

```
git clone https://github.com/Lokeshwaran-M/Jam-AI
cd Jam-AI
```

### Run :

```
python jam-ai.py 2> errors.log
```
> note : to get responces back you need gpt models that needs to be genetated seprately using [lok-lib](https://github.com/Lokeshwaran-M/lok-lib) library model_gen module which uses gpt-2 .documentation on the process will be updated soon

---

## Jam Clients :

### Jam web client :
by [jam web](https://github.com/Lokeshwaran-M/jam-ai.web.git) client we can access jam in browser using jam api
### Jam app client :
by [jam app](https://github.com/Lokeshwaran-M/jam-ai.app.git) client provides android access using jam api

---

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

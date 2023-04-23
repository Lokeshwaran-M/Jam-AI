
import whisper
import sys

model = whisper.load_model("tiny")

# for only english
def transcribe(au_path) :
    
    result = model.transcribe(au_path)
    
    return result["text"]

# for all lang
def transcribe_mul_lang(au_path):
    model = whisper.load_model("base")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(au_path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # print the recognized text
    return result.text



def reg(au_path , type="none"):
    if type=="none":
        res = transcribe(au_path)
    elif type=="mul":
        res = transcribe_mul_lang(au_path)
    return res


if __name__ == "__main__":
    if len(sys.argv) > 1:
        au_path = sys.argv[1]
        print("input audio path :", au_path)
    else:
        au_path = input("Enter audio path : ")
        print("input audio path :", au_path)
    pmt = transcribe(au_path)
    print(pmt)
    


   







        
            


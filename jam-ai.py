
from loklib import audio_recorder as ar
from loklib import speech_reg as sr
from loklib import speech_senth as ss
from loklib import gpt_2 , gn_task
import sys
import os



def listen():
    stop = False
    try:
        while not stop:
            ss.say("listening")
            au_path = ar.record(5, "wav")
            print(au_path)
            pmt = sr.reg(au_path)
            print(pmt)
            if "stop" in pmt.lower():
                stop = True
                ar.close_audio()
                print("stopped")
                # remove audio files
                gn_task.rm_fld("audio")
                ss.say("bye")
                break
            else:
                gpt_res = gpt_2.ans(pmt)
                # brain_res = brain.res(pmt)
                ss.say(gpt_res)

    except Exception as e:
        ar.close_audio()
        print(f"exception occurred : {e}")

def start():
    # check connection
    listen()
    
    
start()











# if __name__ == "__main__":
    

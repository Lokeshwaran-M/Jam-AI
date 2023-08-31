
from loklib import listen
from loklib import speech_senth as ss
from loklib import gn_task 






def observe(t=5):
    res = ""
    try:
        pmt = listen.out(6)
        pmt=pmt.lower()
        print("observed : ",pmt)
        if "stop" in pmt.lower():
            listen.close_audio()
            print("stopped")
             # remove audio files
            gn_task.rm_fld("audio")
            ss.say("bye")
            res = "stop"
        elif "jam" in pmt :
            res = "jam"
            
    except Exception as e:
        listen.close_audio()
        print(f"exception occurred : {e}")

    return res

def listen():
    while True:
        ss.say("listening")
        pmt = listen.out(6)
        
        if "stop" in pmt.lower():
            break
        print("cmd : ",pmt)
        res = f"listned : {pmt}"
        print("jam : ",res)
        ss.say(str(res))


def start():
    print("observing")
    while True:
        ob =observe(4)
        if ob == "jam":
            listen()
        elif ob == "stop":
            break
    

def jam():
    try:
        start()
    except Exception as e:
        listen.close_audio()
        print(f"exception occurred : {e}")



if __name__ == '__main__':
    jam()




    
    

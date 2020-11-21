#from bin.get_dirs import FILE_USR_DATA
from bin.get_dirs import FILE_USR_DATA
import os

from bin import get_dirs
from bin import clear
#import get_dirs
#import clear

def inpt(text = ">>> ", sound = False, audio_io = True, iterate = True, processed = True):
    if audio_io:
        from bin import voice_io
        #import voice_io
        
        while True:
            try:
                entered_data = input(text)
                # voice_io.show("input = ",entered_data)
                
                if entered_data == "voice":
                    i = 0
                    voice_data = False
                    while not voice_data:
                        try:
                            voice_io.show("I am listening......", sound = sound)
                            voice_data = entered_data = voice_io.voice_in()
                            i += 1
                            if i >= 1:
                                voice_io.show("\nSorry, could not get that! Please try again..\n", sound = sound)
                    
                        except KeyboardInterrupt:#stops voice input when ctrl+c is pressed 
                            voice_io.show("\nStopped listening", sound = sound)
                            entered_data = ""
                            voice_data = True

                elif entered_data == "":
                    if not iterate:
                        return ""                         
                    continue

                elif "clear" in entered_data.lower() or entered_data.lower() in "clrcls":
                    return "clear"

                elif entered_data.lower() in ["exit", "quit", "end", "bye", "good bye", "goodbye", "tata"]:
                    #voice_io.show(entered_data.lower() in "exitquitend")
                    voice_io.show("\nBye and have a nice day!", sound = sound)
                    exit()

                else:
                    if processed:
                        entered_data = processData(entered_data)
                    print(entered_data)
                    return entered_data

            except KeyboardInterrupt:#exits from the program when ctrl+c is pressed
                voice_io.show("\nBye and have a nice day!", sound = sound)
                exit()
            
    else:
        entered_data = input(text)
        if processed:
            entered_data = processData(entered_data)

        return entered_data

def processData(data):
    lst = data.split(" ")
    data = ""
    for i in lst:
        n = ""
        if i == " " or i == "":
            continue
        
        for j in i:
            if j.isalnum():
                n += j 

        data += " " + n
    
    return data.strip()
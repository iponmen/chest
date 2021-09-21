import glb
import time
import sys
import os
import _thread as thread
from imports import general

def cmdThead():
    while(glb.running):
        sinput = input("")
        if sinput == "printBoard":
            print(general.consolePrintBoard())
        elif sinput == "exit" or sinput == "stop" or sinput == "quit":
            break
    print(f"Program Quitted - on: { time.ctime(time.time())}")
    os._exit(1)
    # thread.interrupt_main() # this is safer but leaves warnings in the console, so you can't control me
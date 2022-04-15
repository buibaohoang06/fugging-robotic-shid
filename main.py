from pyfirmata import Arduino
import pyfirmata
import time
from fastapi import FastAPI
import json


app = FastAPI()
board = Arduino('/dev/tty.usbserial-110')
led = board.get_pin('d:7:o')


#for testing purposes: when a face is detected, an led will light up
@app.get("/face_check")
def check():
    with open('shid.json', 'r') as shid:
        status = json.loads(shid.read())['status']
    if status == True:
        led.write(1)
    elif status == False:
        led.write(0)
    return {status} 
@app.get("/status")
def status():
    return {"coom"}
    

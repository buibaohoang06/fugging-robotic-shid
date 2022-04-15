from pyfirmata import Arduino
import pyfirmata
import time
from fastapi import FastAPI
import json


app = FastAPI()
board = Arduino('/dev/tty.usbserial-110')
led = board.get_pin('d:7:o')



@app.get("/readcurrent")
def read_light_sensor():
    it = pyfirmata.util.Iterator(board)
    it.start()
    board.analog[2].enable_reporting()
    while True:
        status = board.analog[2].read()
        if status == None:
            time.sleep(1)
            continue
        else:
            break
    if status > 0.8:
        type = "Bright"
    elif status > 0.6 and status < 0.8:
        type = "Normal"
    else:
        type = "Dark"
    return {"status": status, "Type": type}

@app.get("/checksurroundings")
def check():
    lights_on = False
    it = pyfirmata.util.Iterator(board)
    it.start()
    board.analog[2].enable_reporting()
    while True:
        status = board.analog[2].read()
        if status == None:
            time.sleep(1)
            continue
        else:
            break
    if status > 0.8:
        led.write(0)
        lights_on = False
    elif status > 0.6 and status < 0.8:
        led.write(0)
        lights_on = False
    else:
        led.write(1)
        lights_on = True
    return {"status": status, "Lights": lights_on}

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
    
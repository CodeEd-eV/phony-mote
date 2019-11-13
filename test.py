from flask import Flask, request, jsonify
from tools.keysim import Sim 

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

webpage = open("Index2.html", "r").read()

s = Sim()

@app.route("/")
def index():
    return webpage.encode()

import pyautogui
import os

@app.route("/shot")
def screenshot():
    print("[screenshot] stored")
    pyautogui.screenshot().save(os.path.join("static","shot.png"))
    return "received"

@app.route("/click", methods=["POST"])
def click():
    data = (request.json)
    posx = data["posx"]
    posy = data["posy"]

    s.m.click(posx, posy, 1)
        
    return "received"


@app.route("/simulate", methods=["POST"])
def simulate():
    data = (request.json)
    val = data["key"]

    print(val)
        
    command = {
            "left": s.pressLeft,
            "right": s.pressRight,
            "up":   lambda: s.tap(s.k.up_key),
            "down":   lambda: s.tap(s.k.down_key),
            }
    selected = command.get(val, lambda: s.k.tap_key(val))

    print(selected())

    return "received"

@app.route("/text", methods=["POST"])
def type():
    data = (request.json)
    val = data["text"]
    print(val)
    print(s.k.type_string(val))
    print(s.k.tap_key("Return"))

    return "received"

def get_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == "__main__":
    import qrcode

    port = 1337
    path = (get_ip() + ":" + str(port))
    img = qrcode.make(path)
    print(path)
    img.show()
    img.save(os.path.join("static", "qr.jpeg"), "JPEG")

    app.run(host= '0.0.0.0', port=port)

from PIL import Image
import numpy as np

import pyautogui
import time
import os
import PIL
import base64
from io import BytesIO
import pyscreeze


t1 = time.time()
shot = pyautogui.screenshot()
print("T: screenshot PYautogui")
print( (time.time() - t1 ) *1000)

t1 = time.time()
shot = pyscreeze.screenshot()
print("T: screenshot pyscreeze")
print( (time.time() - t1 ) *1000)

t1 = time.time()
buffered = BytesIO()
shot.save(buffered, format="JPEG")
print("T: save")
print( (time.time() - t1 ) *1000)


t1 = time.time()
b = base64.b64encode(buffered.getvalue())
print("T: encode")
print( (time.time() - t1 ) *1000)


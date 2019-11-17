import subprocess
import os
from PIL import Image


def _screenshot_linux_slim():
    tmpFilename = os.path.join("static", "shot.jpeg")
    subprocess.call(['scrot', '-z', tmpFilename])
    im = Image.open(tmpFilename)
    try:
        im.load()
        return im
    except IOError:
        pass # You can always log it to logger
        return None



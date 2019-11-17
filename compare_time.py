
import time
import datetime

import subprocess
from PIL import Image
import os

def time_ms(function, name=""):
    t = time.time()
    out = function()
    print(f"{name} {(time.time() - t ) * 1000} ms")
    return out 

def _screenshot_linux(imageFilename=None, region=None):
    scrotExists = True

    if imageFilename is None:
        tmpFilename = '.screenshot%s.png' % (datetime.datetime.now().strftime('%Y-%m%d_%H-%M-%S-%f'))
    else:
        tmpFilename = imageFilename
    if scrotExists:
        subprocess.call(['scrot', '-z', tmpFilename])
        im = Image.open(tmpFilename)

        if region is not None:
            assert len(region) == 4, 'region argument must be a tuple of four ints'
            region = [int(x) for x in region]
            im = im.crop((region[0], region[1], region[2] + region[0], region[3] + region[1]))
            os.unlink(tmpFilename) # delete image of entire screen to save cropped version
            im.save(tmpFilename)
        else:
            # force loading before unlinking, Image.open() is lazy
            im.load()

        if imageFilename is None:
            os.unlink(tmpFilename)
        return im
    else:
        raise Exception('The scrot program must be installed to take a screenshot with PyScreeze on Linux. Run: sudo apt-get install scrot')

def _screenshot_linux_slim():
    tmpFilename = "trash.jpeg"
    subprocess.call(['scrot', '-z', tmpFilename])
    im = Image.open(tmpFilename)
    im.load()
    return im



if __name__ == "__main__":
    time_ms( _screenshot_linux, "_screenshot_linux" )
    time_ms( _screenshot_linux_slim, "_screenshot_linux_slim" )

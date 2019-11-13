from pymouse import PyMouse
from pykeyboard import PyKeyboard

class Sim:
    
    def __init__(self):
        self.m = PyMouse()
        self.k = PyKeyboard()
    def click(self):
        x_dim, y_dim = self.m.screen_size()
        self.m.click(int(x_dim/2), int(y_dim/2), 1)

    def click(self, x, y):
        self.m.click(int(x), int(y), 1)

    def pressLeft(self):
        self.tap(self.k.left_key)
        return "left"

    def pressRight(self):
        self.tap(self.k.right_key)
        return "right"

    def tap(self, key):
        self.k.tap_key(key)
        return key

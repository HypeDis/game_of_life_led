import unicornhathd as unicorn
import signal
import sys


class UnicornHDController():
    def __init__(self, brightness=0.5, rotation=0):
        unicorn.clear()
        unicorn.brightness(brightness)
        unicorn.rotation(rotation)
        self.height = 16
        self.width = 16
        signal.signal(signal.SIGINT, self.interruptHandler)

    def interruptHandler(self, signum, frame):
        print('app closed')
        unicorn.off()
        sys.exit()

    def inputIsValid(self, x, y, r, g, b):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            return False
        return True

    def setPixel(self, x, y, r, g, b):
        if (self.inputIsValid(x, y, r, g, b)):
            unicorn.set_pixel(x, y, r, g, b)

    def setPixels(self, inputs):
        for input in inputs:
            self.set_pixel(*input)

    def show(self):
        unicorn.show()

    def off(self):
        unicorn.off()
    def clear(self):
        unicorn.clear()

import unicornhathd as unicorn
from time import sleep
from Game import GameOfLife
import signal
import sys

unicorn.clear()
unicorn.brightness(0.5)
unicorn.rotation(0)
width, height = unicorn.get_shape()


def interruptHandler(signum, frame):
    print('app closed')
    unicorn.off()
    sys.exit()


signal.signal(signal.SIGINT, interruptHandler)


def setPixel(cell):
    x, y = cell.getLocation()
    r, g, b = cell.getColor()
    unicorn.set_pixel(x, y, r, g, b)


def main():
    game = GameOfLife(width, height)
    game.randomizeBoard()
    game.forEachCell(setPixel)
    while (game.isPlaying):
        unicorn.show()
        game.updateBoard()
        game.forEachCell(setPixel)
        sleep(0.2)
    unicorn.off()


main()

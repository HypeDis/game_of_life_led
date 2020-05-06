from Game import GameOfLife
import signal
import sys


def main():
    game = GameOfLife.UnicornHDGOL()
    game.LED.clear()
    game.randomizeBoard()
    game.setDuration(30)
    game.setFrameRate(8)
    game.play()


main()

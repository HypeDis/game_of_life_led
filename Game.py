# Any live cell with two or three live neighbors survives.
# Any dead cell with three live neighbors becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

from random import randint
from time import sleep

BLACK_RGB = (0, 0, 0)


class GameOfLife():
    def __init__(self, width, height):
        self.currentColor = (0, 0, 0)
        self.randomizeColor = True
        self.isPlaying = True
        self.width = width
        self.height = height
        self.board = self.initializeBoard()
        self.duration = 60
        self.framesPerSecond = 5

    def initializeBoard(self):
        newBoard = [[Cell(x, y) for x in range(self.width)]
                    for y in range(self.height)]
        return newBoard

    def forEachCell(self, callback):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                cell = self.board[y][x]
                callback(cell)

    def randomizeBoard(self):
        def randomizeCell(cell):
            randbit = randint(0, 1)
            cell.isAlive = not not randbit
            if cell.isAlive:
                cell.color = self.generateRandomColor()
            else:
                cell.color = BLACK_RGB

        self.forEachCell(randomizeCell)

    def play(self):
        sleepTime = 1 / self.framesPerSecond
        totalFrames = self.duation * self.framesPerSecond
        currentFrame = 0
        while currentFrame < totalFrames:
            updateBoard()
            currentFrame += 1
            sleep(sleepTime)


    def generateRandomColor(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

    def setColor(self, r, g, b):
        self.currentColor = (r, g, b)

    def setCell(x, y, rgbColor, aliveStatus):
        if self.isValidCell(x, y):
            cell = self.board[y][x]
            cell.color = rgbColor
            cell.isAlive = aliveStatus

    def getCell(self, x, y):
        return self.board[y][x]

    def updateBoard(self):
        newBoard = self.initializeBoard()
        if self.randomizeColor:
            color = self.generateRandomColor()
            while (sum(color) > 650):
                color = self.generateRandomColor()
            self.currentColor = color
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                updatedCell = self.updateCell(x, y)
                newBoard[y][x] = updatedCell
                if updatedCell.isAlive:
                    self.isPlaying = True
        self.board = newBoard

    def getAliveNeighbors(self, cell):
        # starting from left going around clockwise
        directions = [
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
        ]
        aliveCount = 0
        x, y = cell.getLocation()
        for dX, dY in directions:
            if (self.isValidCell(x + dX, y + dY)):
                neighbor = self.board[y + dY][x + dX]
                if neighbor.isAlive:
                    aliveCount += 1

        return aliveCount

    def copyCell(self, cell):
        x, y = cell.getLocation()
        newCell = Cell(x, y)
        newCell.isAlive = cell.isAlive
        newCell.color = cell.color
        newCell.setLocation(x, y)
        return newCell

    def updateCell(self, x, y):
        cell = self.getCell(x, y)
        newCell = self.copyCell(cell)
        aliveNeighbors = self.getAliveNeighbors(cell)
        if not cell.isAlive and aliveNeighbors == 3:
            newCell.isAlive = True
            newCell.color = self.currentColor
        elif (aliveNeighbors > 3 or aliveNeighbors < 2) and cell.isAlive:
            newCell.color = BLACK_RGB
            newCell.isAlive = False
        return newCell

    def isValidCell(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return True


class Cell():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.isAlive = False
        self.color = (0, 0, 0)

    def setColor(self, rgbColor):
        self.color = rgbColor

    def getColor(self):
        return self.color

    def getLocation(self):
        return (self.__x, self.__y)

    def setLocation(self, x, y):
        self.__x = x
        self.__y = y


# myGame = GameOfLife(5,5)
# myGame.randomizeBoard()
# def getStats(cell):
#     print(cell.isAlive, cell.color)
# myGame.forEachCell(getStats)
# myGame.updateBoard()
# myGame.forEachCell(getStats)
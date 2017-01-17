# TicTacToe.py
# Author: Tinli Yarrington
# Date created: 6/21/15
# Date edited:
# Purpose: to create a game of Tic Tac Toe using graphics
# Notes:
#       - must find easier way to place Xs and Os in midpoint of white boxes as well as finding if there is already a piece there
#       - make sure if piece is already there when clicked, don't switch to next piece

from graphics import *
WIDTH = 600
HEIGHT = 600

class Board:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        self.rect1 = Rectangle(Point(200-w//2, 0), Point(200+w//2, HEIGHT))
        self.rect2 = Rectangle(Point(400-w//2, 0), Point(400+w//2, HEIGHT))
        self.rect3 = Rectangle(Point(0, 200-h//2), Point(WIDTH, 200+h//2))
        self.rect4 = Rectangle(Point(0, 400-h//2), Point(WIDTH, 400+h//2))

    def createBoard(self, win):
        self.rect1.setFill("black")
        self.rect1.draw(win)
        self.rect2.setFill("black")
        self.rect2.draw(win)
        self.rect3.setFill("black")
        self.rect3.draw(win)
        self.rect4.setFill("black")
        self.rect4.draw(win)

class X:
    def __init__(self, xx, yy):
        self.fileName = "__LargeX.gif"
        self.image = Image(Point(xx, yy), self.fileName)
        self.x = xx
        self.y = yy

    def getCenter(self):
        return Point(self.x, self.y)

    def draw(self, win):
        self.image.draw(win)

class O:
    def __init__(self, xx, yy):
        self.fileName = "__BigO.gif"
        self.image = Image(Point(xx, yy), self.fileName)
        self.x = xx
        self.y = yy

    def getCenter(self):
        return Point(self.x, self.y)

    def draw(self, win):
        self.image.draw(win)

def touchBoard(click):
    x = click.getX()
    y = click.getY()

    if (x>=190 and x<=210) or (y>=190 and y<=210) or (x>=390 and x<=410) or (y>=390 and y<=410):
        return False
    else:
        return True

def inWhiteBox(click):
    x = click.getX()
    y = click.getY()

    newX = x
    newY = y

    if (x>=0 and x<=190) and (y>=0 and y<=190):
        newX = 190/2
        newY = 190/2
    elif (x>=0 and x<=190) and (y>=210 and y<=390):
        newX = 190/2
        newY = (210+390)/2
    elif (x>=0 and x<=190) and (y>=410 and y<=600):
        newX = 190/2
        newY = (410+600)/2
    elif (x>=210 and x<=390) and (y>=0 and y<=190):
        newX = (210+390)/2
        newY = 190/2
    elif (x>=210 and x<=390) and (y>=210 and y<=390):
        newX = (210+390)/2
        newY = (210+390)/2
    elif (x>=210 and x<=390) and (y>=410 and y<=600):
        newX = (210+390)/2
        newY = (410+600)/2
    elif (x>=410 and x<=600) and (y>=0 and y<=190):
        newX = (410+600)/2
        newY = 190/2
    elif (x>=410 and x<=600) and (y>=210 and y<=390):
        newX = (410+600)/2
        newY = (210+390)/2
    elif (x>=410 and x<=600) and (y>=410 and y<=600):
        newX = (410+600)/2
        newY = (410+600)/2
    
    return Point(newX, newY)

def hasPiece(pointOfPiece, pieces):
    for piece in pieces:
        if (pointOfPiece.getX() == piece.getCenter().getX()) and (pointOfPiece.getY() == piece.getCenter().getY()):
            return False
    return True

def main():
    # creates a window
    rectWidth = 20
    rectHeight = 20
    win = GraphWin( "Tic Tac Toe", WIDTH, HEIGHT )
    ticTacToeBoard = Board(rectWidth, rectHeight)
    ticTacToeBoard.createBoard(win)

    pieces = []
    alternatePiece = 0
    while True:
        click = win.getMouse()
        if touchBoard(click) and hasPiece(inWhiteBox(click), pieces):
            if alternatePiece%2 == 0:
                placeX = X(inWhiteBox(click).getX(), inWhiteBox(click).getY())
                placeX.draw(win)
                pieces.append(placeX)
            else:
                placeO = O(inWhiteBox(click).getX(), inWhiteBox(click).getY())
                placeO.draw(win)
                pieces.append(placeO)
        alternatePiece = alternatePiece + 1

main()

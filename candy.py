from basic_graphics import *
from tkinter import *
def appStrated(app):
    app.rows =10
    app.cols=10
    app.margin=50

def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1)=getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, fill='white')


def redrawAll(app, canvas):
    drawBoard(app, canvas)
run(width=400, height=400)

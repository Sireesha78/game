from cmu_112_graphics import *
import random

def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.margin = 5
    
def getCellBounds(app, row, col):
    # aka 'modelToView'
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    x0 = app.margin + gridWidth * col / app.cols
    x1 = app.margin + gridWidth * (col+1) / app.cols
    y0 = app.margin + gridHeight * row / app.rows
    y1 = app.margin + gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            if(row<app.rows-2):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='white',outline="Black")
            else:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='white',outline="Black")
            



def redrawAll(app, canvas):
    drawBoard(app, canvas)
    

runApp(width=400, height=400)
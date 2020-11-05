from cmu_112_graphics import *
import random

def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.margin = 10
    app.colors = []
    initFillGrid(app)
    app.selection = (-1, -1)
    app.selected = []

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

def initFillGrid(app):
    colors = ['red', 'blue', 'green', 'yellow']
    for _ in range(app.rows):
        color = random.choices(colors, k=app.cols)
        app.colors.append(color)

    # for col in range(app.cols):
    #     row = 0
    #     while(row<len(app.colors)-2):
    #         if app.colors[row][col] == app.colors[row+1][col] == app.colors[row+2][col]:
    #             app.colors[row][col] = None
    #         else:
    #             row += 1

    # for row in range(app.rows):
    #     col = 0
    #     while(col<len(app.colors)-2):
    #         if app.colors[row][col] == app.colors[row][col+1] == app.colors[row][col+1]:
    #             app.colors[row][col] = None
    #         else:
    #             col += 1

def getCell(app, x, y):
    if app.margin <= x <= app.width - app.margin and app.margin <= y <= app.height - app.margin:
        cellWidth = (app.width - 2 * app.margin) / app.cols
        cellHeight = (app.height - 2 * app.margin) / app.rows
        row = int((y - app.margin) / cellHeight)
        col = int((x - app.margin) / cellWidth)
        return (row, col)

def validMatch(app, row1, col1, row2, col2):
    pass

def swapCells(app):
    r1 = app.selected[0][0]
    c1 = app.selected[0][1]
    r2 = app.selected[1][0]
    c2 = app.selected[1][1]
    if (abs(r1-r2)==1 and c1==c2) or (r1==r2 and abs(c1-c2)==1):
        (app.colors[r1][c1], app.colors[r2][c2]) = (app.colors[r2][c2], app.colors[r1][c1])
    app.selected = []

def mousePressed(app, event):
    (row, col) = getCell(app, event.x, event.y)
    app.selected.append((row, col))
    if len(app.selected)==2:
        swapCells(app)


def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            if (row, col) in app.selected:
                border = 'white'
                thick = 2
            else:
                border = 'black'
                thick = 1
            canvas.create_rectangle(x0, y0, x1, y1, fill=app.colors[row][col], outline=border, width= thick)

        

def redrawAll(app, canvas):
    drawBoard(app, canvas)
    
runApp(width=400, height=400)
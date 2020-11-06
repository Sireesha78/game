from cmu_112_graphics import *
import random

def appStarted(app):
    app.rows = 10                           #number of rows
    app.cols = 10                           #number of columns
    app.margin = 10                         #margins
    app.colors = []                         #will contain colors of cells
    initFillGrid(app)                       #initial random coloring function
    app.selected = []                       #keeps account of selected cells

def initFillGrid(app):
    colors = ['red', 'blue', 'green', 'yellow']             #list of desired colors
    for _ in range(app.rows):
        color = random.choices(colors, k=app.cols)          
        app.colors.append(color)

def getCellBounds(app, row, col):                           #takes row and col, then returns top-left 
    gridWidth  = app.width - 2*app.margin                   #and bottom-right coordinates of a cell
    gridHeight = app.height - 2*app.margin
    x0 = app.margin + gridWidth * col / app.cols
    x1 = app.margin + gridWidth * (col+1) / app.cols
    y0 = app.margin + gridHeight * row / app.rows
    y1 = app.margin + gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def getCell(app, x, y):                                     #finds cell for given coordinates
    if app.margin <= x <= app.width - app.margin and app.margin <= y <= app.height - app.margin:
        cellWidth = (app.width - 2 * app.margin) / app.cols
        cellHeight = (app.height - 2 * app.margin) / app.rows
        row = int((y - app.margin) / cellHeight)
        col = int((x - app.margin) / cellWidth)
        return (row, col)

def mousePressed(app, event):                               #this will happen on a mouse click
    (row, col) = getCell(app, event.x, event.y)                 #get row and col for location of click
    app.selected.append((row, col))
    if len(app.selected)==2:                                    #there are 2 pairs of row and col in app.selected               
        swapCells(app)                                          #call swapCells
        app.selected = []                                       #after swapping set app.selected as empty

def swapCells(app):
    r1 = app.selected[0][0]
    c1 = app.selected[0][1]
    r2 = app.selected[1][0]
    c2 = app.selected[1][1]
    if (abs(r1-r2)==1 and c1==c2) or (r1==r2 and abs(c1-c2)==1):        #if cells are adjacent, swap their colors
        (app.colors[r1][c1], app.colors[r2][c2]) = (app.colors[r2][c2], app.colors[r1][c1])
        if not validMatch5(app, r1, c1, r2, c2) and not validMatch3(app, r1, c1, r2, c2):
            (app.colors[r1][c1], app.colors[r2][c2]) = (app.colors[r2][c2], app.colors[r1][c1])

def validMatch5(app, row1, col1, row2, col2):
    pass

def validMatch3(app, row1, col1, row2, col2):
    return eliminateMatch3(app, row1, col1) or eliminateMatch3(app, row2, col2)

def eliminateMatch3(app, row, col):
    if col>0 and col<app.cols-1:
        coordinates = [(row,col-1), (row, col), (row, col+1)]
        if eliminateCells(app, coordinates):
            return True
    if col<app.cols-2:
        coordinates = [(row,col), (row, col+1), (row, col+2)]
        if eliminateCells(app, coordinates):
            return True
    if col>1:
        coordinates = [(row,col-2), (row, col-1), (row, col)]
        if eliminateCells(app, coordinates):
            return True
    if row>0 and row<app.rows-1:
        coordinates = [(row-1,col), (row, col), (row+1, col)]
        if eliminateCells(app, coordinates):
            return True
    if row<app.rows-2:
        coordinates = [(row,col), (row+1, col), (row+2, col)]
        if eliminateCells(app, coordinates):
            return True
    if row>1:
        coordinates = [(row-2,col), (row-1, col), (row, col)]
        if eliminateCells(app, coordinates):
            return True
    return False

def eliminateCells(app, coordinates):
    c = 0
    row = coordinates[0][0]
    col = coordinates[0][1]
    for loc in coordinates:
        if app.colors[loc[0]][loc[1]]==app.colors[row][col]:
            c += 1
    if c == len(coordinates):
        for loc in coordinates:
            app.colors[loc[0]][loc[1]] = None
        return True
    return False

def redrawAll(app, canvas):                                 #this will be seen on output screen
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            if (row, col) in app.selected:                      #selected cell will be highlighted
                border = 'white'
                thick = 2
            else:
                border = 'black'
                thick = 1
            canvas.create_rectangle(x0, y0, x1, y1, fill=app.colors[row][col], outline=border, width= thick)

runApp(width=400, height=400)

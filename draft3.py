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
        check_gaps(app)
        new_cell(app)

def swapCells(app):
    r1 = app.selected[0][0]
    c1 = app.selected[0][1]
    r2 = app.selected[1][0]
    c2 = app.selected[1][1]
    if (abs(r1-r2)==1 and c1==c2) or (r1==r2 and abs(c1-c2)==1):        #if cells are adjacent, swap their colors
        (app.colors[r1][c1], app.colors[r2][c2]) = (app.colors[r2][c2], app.colors[r1][c1])
        if not validMatch3(app, r1, c1, r2, c2):
            (app.colors[r1][c1], app.colors[r2][c2]) = (app.colors[r2][c2], app.colors[r1][c1])
    
def validMatch3(app, row1, col1, row2, col2):
    if col1 == col2:
        return eliminateColMatch3(app, row1, col1)
    if row1 == row2:
        return eliminateRowMatch3(app, row1, col1)
    return False

def eliminateColMatch3(app, row, col):
    if row>1:
        if app.colors[row-2][col] == app.colors[row-1][col] == app.colors[row][col]:
            app.colors[row-2][col] = None
            app.colors[row-1][col] = None
            app.colors[row][col] = None
            return True
    if row<app.rows-2:
        if app.colors[row+2][col] == app.colors[row+1][col] == app.colors[row][col]:
            app.colors[row+2][col] = None
            app.colors[row+1][col] = None
            app.colors[row][col] = None
            return True
    return False

def eliminateRowMatch3(app, row, col):
    if col>1:
        if app.colors[row][col-2] == app.colors[row][col-1] == app.colors[row][col]:
            app.colors[row][col-2] = None
            app.colors[row][col-1] = None
            app.colors[row][col] = None
            return True
    if col<app.cols-2:
        if app.colors[row][col+2] == app.colors[row][col+1] == app.colors[row][col]:
            app.colors[row][col+2] = None
            app.colors[row][col+1] = None
            app.colors[row][col] = None
            return True
    return False

def drop_cell(app,row,col):
    for r in range(row,0,-1):
        # for col in row:
        # if app.colors[row][r] == app.colors[row-1][r]:
        #         app.colors[0][r]=None
        (app.colors[r][col], app.colors[r-1][col])=(app.colors[r-1][col], app.colors[r][col])


def check_gaps(app):
    for row in range(app.rows):
        for col in range(app.cols):
            if app.colors[row][col] == None:
                drop_cell(app,row,col)
            

def new_cell(app):
    # New_prob=0.9
    # for row in range(app.rows):
    #     if app.colors[0][row] is None and random.random()<New_prob:
    #         app.colors[0][row]=random.randint(1,9)
    color=["red","blue","green","yellow"]
    for row in range(app.rows):
        for col in range(app.cols):
            if app.colors[row][col] == None:
                app.colors[row][col] = random.choice(color)

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

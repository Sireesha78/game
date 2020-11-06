from cmu_112_graphics import *
import random

def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.margin = 10
    fillColors(app)
    app.selection = (-1, -1)

def getCell(app, x, y):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows

    # Note: we have to use int() here and not just // because
    # row and col cannot be floats and if any of x, y, app.margin,
    # cellWidth or cellHeight are floats, // would still produce floats.
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)

    return (row, col)   
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


def pointInGrid(app, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))


def fillColors(app):
    app.colors = []
    for _ in range(app.rows):
        c = []
        for _ in range(app.cols):
            c.append(random.choice(['red', 'blue', 'green', 'yellow']))
        app.colors.append(c)

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, fill=app.colors[row][col] ,outline="black")
# # def cell_pos():
# #     return int(cursor.app.rows // 10)-1 , int(cursor.app.cols // 10)
# def mousePressed(app, event):
#     app.cx = event.x
#     app.cy = event.y
# # def click_key(app,key,canvas):
# #     gridWidth  = app.width - 2*app.margin
# #     gridHeight = app.height - 2*app.margin
# #     app.rows,app.cols= cell_pos()
# #     if key==keys.LEFT and app.rows>0:
# #         cursor.app.rows -= 10
# #     if key==keys.RIGHT and app.rows<gridWidth-2:
# #         cursor.app.rows += 10
# #     if key==keys.LEFT and app.cols>0:
# #         cursor.app.rows -= 10
# #     if key==keys.LEFT and app.cols>gridHeight-1:
# #         cursor.app.rows += 10
# #     if key==keys.SPACE:
# #         canvas[app.cols][app.rows], canvas[app.cols][app.rows+1]=canvas[app.cols][app.rows+1],canvas[app.cols][app.rows]


def check_gaps(app, canvas):
    for col in range(canvas-1,-1,-1):
        for row in range(canvas):
            if canvas[col][row] is None:
                drop_cell(row,col,canvas)

def drop_cell(row,col,canvas):
    for i in range(col,0,-1):
        canvas[i][row]= canvas[i-1][row]
    canvas[0][row]=None
def new_cell(app, canvas):
    New_prob=0
    #for col in range(len(canvas[0])):
    for row in range(app.rows):
        if canvas[0][row] is None and random.random()<New_prob:
            canvas[0][row]=random.randint(1,9)

def mousePressed(app, event):
    (row, col) = getCell(app, event.x, event.y)
    # select this (row, col) unless it is selected
    if (app.selection == (row, col)):
        app.selection = (-1, -1)
    else:
        app.selection = (row, col)




def redrawAll(app, canvas):
    
    # draw grid of cells
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            fill = "black" if (app.selection == (row, col)) else "white"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
    #canvas.create_text(app.width/2, app.height/2 - 15, text="Click in cells!",
                       #font="Arial 26 bold", fill=fillColors)
    # canvas.create_rectangle(0, 0, app.width, app.height, fill="black")
    drawBoard(app, canvas)

runApp(width=400, height=400)
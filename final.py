from cmu_112_graphics import *
import random

def appStarted(app):
    app.startGame = True
    app.gameTime = 60
    app.timerDelay = 1000
    app.gameOver = False
    app.margin = 5
    app.gridCoordinates = (app.margin, 100, app.width-100, app.height-app.margin)
    app.rows = 10
    app.cols = 10
    app.colorGrid = []
    app.colors = ['red', 'blue', 'green', 'yellow']
    initGrid(app)
    app.selected = []
    app.scores = []
    app.restart = False

score = 0           #global variable for storing and updating scores

# This function initialises the grid for the game
def initGrid(app):
    global score
    for _ in range(app.rows):
        color = random.choices(app.colors, k=app.cols)          
        app.colorGrid.append(color)
    while(checkMatches(app)!=0):
        pass
    score = 0 

# This function checks for matches present in the field
def checkMatches(app):
    global score
    c = 0
    for row in range(app.rows):
        for col in range(app.cols):
            if eliminateMatch5(app, row, col): 
                checkGaps(app)
                newCells(app)
                c += 1
                score += 2
            elif eliminateMatch3(app, row, col):
                checkGaps(app)
                newCells(app)
                c += 1
                score += 2
    return c

# This function checks if there are gaps (None) in the field --helper function for dropCells
def checkGaps(app):
    for row in range(app.rows):
        for col in range(app.cols):
            if app.colorGrid[row][col] == None:
                dropCells(app,row,col)

# This function drops the cells from top in gaps are present in the field 
def dropCells(app, row, col):
    for r in range(row,0,-1):
        (app.colorGrid[r][col], app.colorGrid[r-1][col])=(app.colorGrid[r-1][col], app.colorGrid[r][col])

# This function generates new cells to fill the gaps (None)
def newCells(app):
    for row in range(app.rows):
        for col in range(app.cols):
            if app.colorGrid[row][col] == None:
                app.colorGrid[row][col] = random.choice(app.colors)

# This function eliminates match 5 if given cell is part of it
def eliminateMatch5(app, row, col):
    if col>1 and col<app.cols-2:
        coordinates = [(row, col-2),(row,col-1), (row, col), (row, col+1),(row, col+2)]
        if eliminateCells(app, coordinates):
            return True
    if row>1 and row<app.rows-2:
        coordinates = [(row-2, col),(row-1,col), (row, col), (row+1, col),(row+2, col)]
        if eliminateCells(app, coordinates):
            return True  

# This function eliminates match 3 if given cell is part of it
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

# This function eliminates given list of cells (set them to None), if they are same --helper function 
def eliminateCells(app, coordinates):
    c = 0
    row = coordinates[0][0]
    col = coordinates[0][1]
    for loc in coordinates:
        if app.colorGrid[loc[0]][loc[1]]==app.colorGrid[row][col]:
            c += 1
    if c == len(coordinates):
        for loc in coordinates:
            app.colorGrid[loc[0]][loc[1]] = None
        return True
    return False

# This function swaps two adjacent cells
def swapCells(app):
    global score
    r1 = app.selected[0][0]
    c1 = app.selected[0][1]
    r2 = app.selected[1][0]
    c2 = app.selected[1][1]
    if (abs(r1-r2)==1 and c1==c2) or (r1==r2 and abs(c1-c2)==1):        
        (app.colorGrid[r1][c1], app.colorGrid[r2][c2]) = (app.colorGrid[r2][c2], app.colorGrid[r1][c1])
        if not validMatch5(app, r1, c1, r2, c2) and not validMatch3(app, r1, c1, r2, c2):       
            (app.colorGrid[r1][c1], app.colorGrid[r2][c2]) = (app.colorGrid[r2][c2], app.colorGrid[r1][c1])
        if validMatch5(app, r1, c1, r2, c2):
            score += 2
        elif validMatch3(app, r1, c1, r2, c2):
            score += 1

# This function checks if excuted swap is valid match 5 move
def validMatch5(app, row1, col1, row2, col2):
    return eliminateMatch5(app, row1, col1) or eliminateMatch5(app, row2, col2)    

# This function checks if excuted swap is valid match 3 move
def validMatch3(app, row1, col1, row2, col2):
    return eliminateMatch3(app, row1, col1) or eliminateMatch3(app, row2, col2)

# This function returns highscore for a given run
def getHighscore(app):
    return max(app.scores)
 
# This function returns row and col of the cell for given coordinates
def getCell(app, x, y):
    (x0, y0, x1, y1) = app.gridCoordinates
    if x0 <= x <= x1 and y0 <= y <= y1:
        cellWidth = (x1-x0) / app.cols
        cellHeight = (y1-y0) / app.rows
        row = int((y - y0) / cellHeight)
        col = int((x - x0) / cellWidth)
        return (row, col)
    else:
        return (-1, -1)

# This function returns top-left and bottom-right coordinates for a given cell
def getCellBounds(app, row, col):
    gridWidth  = app.gridCoordinates[2] - app.gridCoordinates[0]
    gridHeight = app.gridCoordinates[3] - app.gridCoordinates[1]
    x0 = app.gridCoordinates[0] + gridWidth * col / app.cols
    x1 = app.gridCoordinates[0] + gridWidth * (col+1) / app.cols
    y0 = app.gridCoordinates[1] + gridHeight * row / app.rows
    y1 = app.gridCoordinates[1] + gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)


# This function describes the working of the app when a mouse click takes place
def mousePressed(app, event):
    global score
    # if game has not started, start the game
    if app.startGame:
        app.startGame = False
    else:
        (row, col) = getCell(app, event.x, event.y)
        if (row, col) != (-1, -1):               
            app.selected.append((row, col))
            if len(app.selected)==2:                                   
                swapCells(app)                                         
                app.selected = []                                      
            while(checkMatches(app)!=0):
                pass
    if app.gameOver:
        app.gameOver = False
        app.restart = True
        app.gameTime = 60
        score = 0

# This function describes how the timer is working in the app
def timerFired(app):
    # if game is started, then only start the timer
    if not app.startGame or app.restart:
        # if countdown reached zero, the set game over
        if app.gameTime == 0:
            app.gameOver = True
            app.scores.append(score)
            return
        app.gameTime -= 1

# This function designs the welcome screen of the game
def startScreen(app, canvas):                 
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'orange')
    navy = f'#{00:02x}{00:02x}{80:02x}'
    text_size = app.width//8
    canvas.create_text(app.width/2, app.height/4, text = "Match - 3", fill = navy, font = f'Times {text_size} bold')
    text_size = app.width//20
    canvas.create_text(app.width/2, app.height/2, text = "Click any where to Start!", fill = navy, font = f'Times {text_size} bold')

# This function designs basic layout after starting the game
def gameBase(app, canvas):
    navy = f'#{00:02x}{00:02x}{80:02x}'
    canvas.create_rectangle(0, 0, app.width, app.height, fill = navy)
    canvas.create_text(app.width/2, 50, text = "Match - 3 Puzzle", fill = 'orange', font = 'Times 40 bold')
    canvas.create_text(app.width-50, app.height/4, anchor='s', text = 'Time', fill = 'orange', font = 'Times 20')
    canvas.create_text(app.width-50, app.height/4, anchor='n', text = str(app.gameTime), fill = 'orange', font = 'Times 20')
    canvas.create_text(app.width-50, app.height/2, anchor='s', text = 'Score', fill = 'orange', font = 'Times 20')
    canvas.create_text(app.width-50, app.height/2, anchor='n', text = str(score), fill = 'orange', font = 'Times 20')
    canvas.create_rectangle(app.margin, 100, app.width-100, app.height-app.margin, outline = 'orange', width = 5)

# This function designs the actual area where game takes place
def gameBoard(app, canvas):
    navy = f'#{00:02x}{00:02x}{80:02x}'
    canvas.create_rectangle(app.margin, 100, app.width-100, app.height-app.margin, fill = 'black')
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            if (row, col) in app.selected:                      #selected cell will be highlighted
                border = 'white'
                thick = 3
            else:
                border = navy
                thick = 1
            canvas.create_oval(x0, y0, x1, y1, fill=app.colorGrid[row][col], outline=border, width= thick)

# This function designs game over screen
def overScreen(app, canvas):
    global score
    if app.gameOver:
        canvas.create_rectangle(0, 0, app.width, app.height, fill = 'orange')
        navy = f'#{00:02x}{00:02x}{80:02x}'
        text_size = app.width//8
        canvas.create_text(app.width/2, app.height/4, text = "Game Over!!", fill = navy, font = f'Times {text_size} bold')
        total = 'Your Score: ' + str(score)
        highscore = 'HighScore: ' + str(getHighscore(app))
        canvas.create_text(app.width/2, app.height/2, anchor='s', text = total, fill = navy, font = 'Times 30')
        canvas.create_text(app.width/2, app.height/2, anchor='n', text = highscore, fill = navy, font = 'Times 30')
        text_size = app.width//20
        canvas.create_text(app.width/2, 3*app.height/4, text = "Click any where to Restart!", fill = navy, font = f'Times {text_size} bold')

def redrawAll(app, canvas):
    if app.startGame:
        startScreen(app, canvas)
    else:
        gameBase(app, canvas)
        gameBoard(app, canvas)
        overScreen(app, canvas)

runApp(width=500, height=500)

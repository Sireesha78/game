import random

rows = 10
cols = 10

colorGrid = []
colors = ['red', 'blue', 'green', 'yellow'] 

for _ in range(rows):
    color = random.choices(colors, k=cols)
    colorGrid.append(color)

for row in range(rows):
    col = 0
    while(col<cols-2):
        if colorGrid[row][col] == colorGrid[row][col+1] == colorGrid[row][col+2]:
            colorGrid[row][col] = None
        else:
            col += 1

for col in range(cols):
    row = 0
    while(row<rows-2):
        if colorGrid[row][col] == colorGrid[row+1][col] == colorGrid[row+2][col]:
            colorGrid[row][col] = None
        else:
            row += 1

def printGrid(grid):
    for r in grid:
        for c in r:
            if c == None:
                c = "None"
            print(c.rjust(8), end=" ")
        print()

def drop_cell(grid, row,col):
    for r in range(row,0,-1):
        # for col in row:
        # if app.colors[row][r] == app.colors[row-1][r]:
        #         app.colors[0][r]=None
        (grid[r][col], grid[r-1][col])=(grid[r-1][col],grid[r][col])


def check_gaps(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == None:
                drop_cell(grid, row,col)

printGrid(colorGrid)
check_gaps(colorGrid)
print("---------------------")
printGrid(colorGrid)

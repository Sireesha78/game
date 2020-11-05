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

printGrid(colorGrid)

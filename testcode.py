<<<<<<< HEAD
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
=======
# import random

# rows = 10
# cols = 10

# colorGrid = []
# colors = ['red', 'blue', 'green', 'yellow'] 

# for _ in range(rows):
#     color = random.choices(colors, k=cols)
#     colorGrid.append(color)

# for row in range(rows):
#     col = 0
#     while(col<cols-2):
#         if colorGrid[row][col] == colorGrid[row][col+1] == colorGrid[row][col+2]:
#             colorGrid[row][col] = None
#         else:
#             col += 1

# for col in range(cols):
#     row = 0
#     while(row<rows-2):
#         if colorGrid[row][col] == colorGrid[row+1][col] == colorGrid[row+2][col]:
#             colorGrid[row][col] = None
#         else:
#             row += 1

# def printGrid(grid):
#     for r in grid:
#         for c in r:
#             if c == None:
#                 c = "None"
#             print(c.rjust(8), end=" ")
#         print()

# printGrid(colorGrid)


# l = [1, 1, 1, 1, 2, 3, 4, 5, 3, 3]
# # print(l[-2:].count(3))
# # print(len(l[-2:]))
# # if l[-2:].count(3)==len(l[-2:]):
# #     for n in range(len(l[-2:])):
# #         # print(n)
# #         l[-2+n] = 4
# l[-2:] = [0]*len(l[-2:])
# print(l)

cordi = [(1,3),(4,2)]
# print(type(cordi[0][0]))
# print(cordi[0][1])
# print(cordi[1][0])
# print(cordi[1][1])
for loc in cordi:
    print(loc[0])
    print(loc[1])


>>>>>>> 5e827fec52b9371e14808f366ea2b16ac5d15297

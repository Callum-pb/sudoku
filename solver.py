# Solve Sudoku puzzle from given 2D-array

# import numpy as np

# #Example grid
# startingGrid = [[0,2,0,0,0,4,3,0,0],
#                 [9,0,0,0,2,0,0,0,8],
#                 [0,0,0,6,0,9,0,5,0],
#                 [0,0,0,0,0,0,0,0,1],
#                 [0,7,2,5,0,3,6,8,0],
#                 [6,0,0,0,0,0,0,0,0],
#                 [0,8,0,2,0,5,0,0,0],
#                 [1,0,0,0,9,0,0,0,3],
#                 [0,0,9,8,0,0,0,6,0]]

#grid = np.copy(startingGrid)


# class Solve():
#     def __init__(self,parent):
#         self.parent = parent
#         self.unsolved = grid
#         self.solved = []
        
        
#     def SolveGrid(self):
#         #Find index of blank cell
#         if not self.blankCell():
#             self.solved = np.copy(self.unsolved)
#             return self.solved
#         r,c = self.blankCell()
#         #Try numbers in blank cell
#         for n in range(1,10):
#             #If number valid, set the cell value to that number
#             if ValidInput(r,c,n):
#                 self.unsolved[r][c] = n
#                 #Keep solving
#                 if SolveGrid(self):
#                     return True
#                 #If a dead end is reached, set the cell to zero and go back a cell
#                 self.unsolved[row][col] = 0
#         #If no numbers are valid, return false to go back a cell
#         return False

#     #Check input is valid
#     def validInput(self, r, c, n):
#         #Check row
#         for col_index in range(9):
#             if self.unsolved[r][col_index] == n:
#                 return False
#         #Check column
#         for row_index in range(9):
#             if self.unsolved[row_index][c] == n:
#                 return False
#         #Check 3x3 block
#         r0 = (r//3)*3 # Find row index of upper left corner of 3x3 block
#         c0 = (c//3)*3 # Find col index of upper left corner of 3x3 block
#         #Run through each cell in 3x3 block
#         for i in range(3):
#             for j in range(3):
#                 if self.unsolved[r0+i][c0+j] == n:
#                     return False
#         #If it makes it this far then it is a valid valid input
#         return True
        
#     #Find empty cells
#     def blankCell(self):
#         for i in range(9):
#             for j in range(9):
#                 if self.unsolved == 0:
#                     return (i,j)
#         return False
        
# Solve Sudoku puzzle from given 2D-array

import numpy as np

#Takes np.matrix element
def solve_grid(grid):
    #Find index of blank cell
    if not blankCell(grid):
        solved = np.copy(grid)
        return True
    r,c = blankCell(grid)
    #Try numbers in blank cell
    for n in range(1,10):
        #If number valid, set the cell value to that number
        if valid_input(grid,r,c,n):
            grid[r][c] = n
            #Keep solving
            if solve_grid(grid):
                return True
            #If a dead end is reached, set the cell to zero and go back a cell
            grid[r][c] = 0
    #If no numbers are valid, return false to go back a cell
    return False

#Check input is valid
def valid_input(grid, r, c, n):
    #Check row
    for col_index in range(9):
        if grid[r][col_index] == n:
            return False
    #Check column
    for row_index in range(9):
        if grid[row_index][c] == n:
            return False
    #Check 3x3 block
    r0 = (r//3)*3 # Find row index of upper left corner of 3x3 block
    c0 = (c//3)*3 # Find col index of upper left corner of 3x3 block
    #Run through each cell in 3x3 block
    for i in range(3):
        for j in range(3):
            if grid[r0+i][c0+j] == n:
                return False
    #If it makes it this far then it is a valid valid input
    return True
        
#Find empty cells
def blankCell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i,j)
    return False

# #Example grid
# startingGrid = [[0,2,0,0,0,4,3,0,0],
#                 [9,0,0,0,2,0,0,0,8],
#                 [0,0,0,6,0,9,0,5,0],
#                 [0,0,0,0,0,0,0,0,1],
#                 [0,7,2,5,0,3,6,8,0],
#                 [6,0,0,0,0,0,0,0,0],
#                 [0,8,0,2,0,5,0,0,0],
#                 [1,0,0,0,9,0,0,0,3],
#                 [0,0,9,8,0,0,0,6,0]]
                
# startingGrid = np.matrix(startingGrid)

# print(startingGrid)

# grid = np.copy(startingGrid)

# solve_grid(grid)

# print(grid)



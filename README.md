# Sudoku

The notebook was an initial exploration into how to solve a sudoku board

The solver.py file contains the completed backtracking functions required to solve a board in a 2D-array format.

The testing.py file contains the Tkinter GUI that displays an interactive window. The window allows a user to input a Sudoku board and request a solved board in return. It also allows a user to load a predefined board. This can also be solved. The user can also input their own answer and check their solution.

The future features will include a better designed UI. A dictionary of multiple starting files that can be selected/played based on a difficulty level. Initially these puzzles will be imported from online sources. Eventually, I will be creating my own using a random seed and solving the board. Then removing cells to create starting puzzles for a given difficulty.

The GUI will eventually be the control area for importing puzzles based on camera images. A ML-algorithm will then detect the puzzle within an image and pull out the starting grid.

The software will also become more flexiable, allowing different sized Sudoku boards, not just the traditional 9x9.

The GUI will then be combined with other puzzle-based projects of a similar scope. Creating one central piece of software that allows the playing, uploading, and solving of many different puzzle types. The other puzzle type I'm currently working on is the _Battleships_ logic puzzle. 

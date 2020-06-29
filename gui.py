#window_width=290
#window_height=310
##button_height = window_height-window_width
#root.geometry('{}x{}'.format(window_width,window_height))

import tkinter as tk
import numpy as np
import solver

class MainWindow(tk.Frame):
    def __init__(self,window,*args,**kwargs):
        tk.Frame.__init__(self,window,*args,**kwargs)
        self.window = window
        #Load Menu Bar
        #self.main_menu = tk.Menu(self)
        self.DisplayMenu()
        #Load frames into window
        self.DisplayContainers()
        
    def DisplayMenu(self):
        #Create menu bar
        self.main_menu = tk.Menu(root)
        #Create menu items
        self.main_menu.add_command(label='Puzzle')
        self.main_menu.add_command(label='Options')
        self.main_menu.add_command(label='Exit')
        #disply menu
        root.config(menu=self.main_menu)


    def DisplayContainers(self):
        #Create containers for window layout
        puzzle_frame = Board(self)
        buttons_frame_top = tk.Frame(self,pady=5)
        buttons_frame_bottom = tk.Frame(self,pady=5)

        #Place main window containers
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        buttons_frame_top.grid(row=0,sticky='ew')
        puzzle_frame.grid(row=1,sticky='nsew')
        buttons_frame_bottom.grid(row=2,sticky='ew')

        #Create buttons for top buttons frame
        reset_btn = tk.Button(buttons_frame_top,text='Reset',command=puzzle_frame.reset_puzzle)
        clear_btn = tk.Button(buttons_frame_top,text='Clear',command=puzzle_frame.clr_board)
        check_btn = tk.Button(buttons_frame_top,text='Check',command=puzzle_frame.check_puzzle)
        solve_btn = tk.Button(buttons_frame_top,text='Solve',command=puzzle_frame.solve_board)

        #Make buttons expand with window
        buttons_frame_top.rowconfigure(0,weight=1,minsize=10)
        for i in range(4):
            buttons_frame_top.columnconfigure(i,weight=1,minsize=40)

        #Place buttons in buttons_frame_top
        reset_btn.grid(row=0,column=0,sticky='ew')
        clear_btn.grid(row=0,column=1,sticky='ew')
        check_btn.grid(row=0,column=2,sticky='ew')
        solve_btn.grid(row=0,column=3,sticky='ew')


        #Create buttons for bottom buttons frame
        solve_btn = tk.Button(buttons_frame_bottom,text='Solve',command=puzzle_frame.solve_board)
        clear_btn = tk.Button(buttons_frame_bottom,text='Clear',command=puzzle_frame.clr_board)
        load_btn = tk.Button(buttons_frame_bottom,text='Load',command=puzzle_frame.load_puzzle)
        save_btn = tk.Button(buttons_frame_bottom,text='Save',command=puzzle_frame.save_grid)

        #Make buttons expand with window
        buttons_frame_bottom.rowconfigure(0,weight=1,minsize=10)
        for i in range(4):
            buttons_frame_bottom.columnconfigure(i,weight=1,minsize=40)

        #Place buttons in buttons_frame_bottom
        solve_btn.grid(row=0,column=0,sticky='ew')
        clear_btn.grid(row=0,column=1,sticky='ew')
        load_btn.grid(row=0,column=2,sticky='ew')
        save_btn.grid(row=0,column=3,sticky='ew')


class Board(tk.Frame):
    def __init__(self,window,*args,**kwargs):
        tk.Frame.__init__(self,window,*args,**kwargs)
        self.window = window
        
        #Initate function for validation command
        vcmd = (self.register(self._validate),'%P')

        #Containers arrays for cells, values, and puzzle states
        self.cells = []             #For cell elements - will be 1D array of length 81
        self.cell_values = []       #For the cell values (used for check)
        self.starting_puzzle = []   #For the loaded puzzle at start (used for solve)
        self.solved_puzzle = []     #Final solved puzzle for display and check
        
        
        #Create widgets for Board Frame
        for row in range(81):
            self.cells.append(tk.Entry(self,width=2,justify='center', relief=tk.GROOVE,     borderwidth=3, font='18',validate='key',vcmd=vcmd))

        #Make the grid expand with the window
        for i in range(9):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        
        #Place widgets in Board
        for i in range(len(self.cells)):
            row_index = i // 9
            column_index = i % 9
            self.cells[i].grid(row=row_index,column=column_index)
            #Colour grid for blocks
            if (row_index in (0,1,2,6,7,8) and column_index in (0,1,2,6,7,8)) or (row_index in (3,4,5) and column_index in (3,4,5)):
                self.cells[i].configure(bg='light blue')
    
            
    #Validate command for limiting each cell entry to digits 0-9
    def _validate(self,P):
        '''
        This limites the text input to just single digits. I need to allow the empty string input in the second statement to allow the delete function to work. The delete function effictively inputs an empty string, which would be rejected by the validate without this explicit allowance of the strip funciton. To then stop just the space bar being entered, this is rejected as the first statement.
        '''
        
        if P == ' ':
            return False
        if P.strip() == '':
            return True
        if len(P) != 1:
            return False

        try:
            f = int(P)
        except ValueError:
            self.bell()
            return False
        return True

    #Solve the puzzle using solver.py functions
    def solve_board(self):
        #If starting_puzzle empty, set it to current cell values
        if len(self.starting_puzzle) == 0:
            self.get_values()               #Update array
            temp = self.cell_values.copy()  #Get copy of array to format
            for i in range(len(temp)):      # Replace any blanks with 0's
                if temp[i] == '':
                    temp[i] = 0
                temp[i] = int(temp[i])        #Convert entries from str to int
            temp = np.array(temp).reshape(9,9)#Create a 9x9 matrix for starting_puzzle
            self.starting_puzzle = temp       #Set starting puzzle
            
        #Test for uniqueness or enough information (17 starting cells)
        #Solve the puzzle
        self.display_starting_puzzle()
        unsolved = self.starting_puzzle.copy()
        solver.solve_grid(unsolved)
        #Display the solution
        solved = unsolved.flatten()
        self.fill_cells(solved)
        
        
    

    #Fill cells with values (used for load and solve to display puzzle)
    def fill_cells(self,values):
        for i in range(len(values)):
            self.cells[i].delete(0,'end')
            if values[i] == 0:
                self.cells[i].insert(0,'')
            else:
                self.cells[i].insert(0,values[i])
            #Reset cell_values array
            self.get_values()

    #Get values from board into array (used in solve and save) (empty cells left as '')
    def get_values(self):
        self.cell_values = []
        for cell in range(len(self.cells)):
            self.cell_values.append(self.cells[cell].get())

    #Convert matrix to 1D array then set starting_puzzle, then fill grid with puzzle
    def display_starting_puzzle(self):
        tmp = self.starting_puzzle.flatten()
        self.fill_cells(tmp)
        for i in range(len(self.cells)):
            if not (self.cell_values[i] == ''):
                self.cells[i].configure(state=tk.DISABLED)
                
                ######## Methods for Buttons ##########
  
    #Delete contents of each cell in Board frame
    def clr_board(self):
        for cell in range(len(self.cells)):
            self.cells[cell].configure(state=tk.NORMAL)
            self.cells[cell].delete(0,'end')
            #reset storage arrays
            self.cell_values = []
            self.starting_puzzle = []
  
    #Load function - fill each cell with starting values
    def load_puzzle(self):
        self.starting_puzzle = np.array([[0,2,0,0,0,4,3,0,0],
                                        [9,0,0,0,2,0,0,0,8],
                                        [0,0,0,6,0,9,0,5,0],
                                        [0,0,0,0,0,0,0,0,1],
                                        [0,7,2,5,0,3,6,8,0],
                                        [6,0,0,0,0,0,0,0,0],
                                        [0,8,0,2,0,5,0,0,0],
                                        [1,0,0,0,9,0,0,0,3],
                                        [0,0,9,8,0,0,0,6,0]])
        temp = self.starting_puzzle.copy()
        solver.solve_grid(temp)
        self.solved_puzzle = temp
        self.display_starting_puzzle()
   
    #Save the board to a 2D matrix. This function is called by the save button.
    def save_grid(self):
        self.get_values()
        #Take the list and create a np matrix whilst filling in '' with 0 to create array
        for i in range(len(self.cell_values)):
            if self.cell_values[i] == '':
                self.cell_values[i] = 0
            self.cell_values[i] = int(self.cell_values[i])
        self.cell_values = np.matrix(self.cell_values).reshape(9,9)
        print(np.array(self.cell_values))

    #Clears user entries and displays just the starting puzzle
    def reset_puzzle(self):
        print('reset')
    #     self.clr_board()
    #     if len(self.starting_puzzle) > 0:
    #         self.load_puzzle()

    #Checks user entries against solution
    def check_puzzle(self):
    #     self.get_values()
    #     solved_array = self.solved_puzzle.flatten()
    #     for i in range(len(self.cell_values)):
    #         if self.cell_values[i] != solved_array[i]:
    #             self.cells[i].configure(bg='red')
        print('checking')



if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side='top',fill='both',expand=True)
    root.mainloop()
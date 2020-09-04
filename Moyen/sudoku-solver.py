import sys
import math


class Cell:
  """
    Init the cell
  """
  def __init__(self,row,col,val,game):
    self.row = row
    self.col = col
    self.pos = (self.row,self.col)
    self.value = val
    self.solved = True if self.value > 0 else False           
    self.current_test_index = 0                     #Index of the value we testin'
    self.game = game                          #Parent link
    self.potential_values = set(range(1,10)) if not self.solved else [] #potential values for the cell


    if not self.solved:
      self.findPotentialValues()

  def __str__(self):
    return f"{self.row},{self.col} : {self.value} \t Solved:{self.solved}"

  # Find all potential values for this cell
  def findPotentialValues(self):
    for item in self.game.getRow(self.pos) + self.game.getCol(self.pos) + self.game.getSquare(self.pos):
      if item in self.potential_values:
        self.potential_values.remove(item)
    self.potential_values = list(self.potential_values)
    self.handle_unique_value()


  # If only one value possible, set it, and mark the cell as solved
  def handle_unique_value(self):
    if len(self.potential_values) == 1:
      self.set_value()
      self.solved = True

  def set_value(self):
    if not self.solved:
      self.value = self.potential_values[self.current_test_index]
      self.game.board[self.row][self.col] = self.value


  def increment(self):
    while not self.is_valid_number() and self.current_test_index < len(self.potential_values) - 1:
      self.current_test_index += 1
      self.set_value()

  def is_valid_number(self):
    """checks to see if the current number is valid in its row, column, and box"""
    for condition in [self.game.getRow(self.pos), self.game.getCol(self.pos), self.game.getSquare(self.pos)]:
      if not self.check_alignement_condition(condition):
        return False
    return True

  def check_alignement_condition(self,condition):
    values = [value for value in condition if value != 0]
    return len(values) == len(set(values)) # Set doesn't take double into account, so if we have 2 '1' on the same row, comparison will be false




class Sudoku:
  def __init__(self,initial_board):
    self.board = initial_board #List of list of int

    self.solve_cells = [] #List of cells for the board

    self.backtrack_index = 0 #Index for backtracking algorithm
    self.initialize_solved_board()
  
  def __str__(self):
    res = ""
    for row in self.board:
      res = res + "".join([str(r) for r in row]) +"\n"
    return res[:-1] # We skip the last \n

  """
    Info part
  """

  def getRow(self,pos):return [self.board[pos[0]][x] for x in range(9)]

  def getCol(self,pos):return [self.board[y][pos[1]] for y in range(9)]

  def getSquare(self,pos):
    lX, lY, hX, hY = 0,0,0,0
    if pos[0] % 3 == 0:
      lY = pos[0]
      hY = pos[0]+2
    elif pos[0] % 3 == 1:
      lY = pos[0]-1
      hY = pos[0]+1
    else:
      lY = pos[0]-2
      hY = pos[0]
    
    if pos[1]%3 == 0:
      lX = pos[1]
      hX = pos[1]+2
    elif pos[1]%3 == 1:
      lX = pos[1]-1
      hX = pos[1]+1
    else:
      lX = pos[1]-2
      hX = pos[1]
    square = []
    for j in range(lY,hY+1,1):
      for i in range(lX,hX+1,1):
        square.append(self.board[j][i])
    return square



  """
    Algorithm Part
  """
  def initialize_solved_board(self):
    for j,row in enumerate(self.board):
      for i,value in enumerate(row):
        self.solve_cells.append(Cell(j,i,value,self))

  def solve(self):
    while self.backtrack_index < len(self.solve_cells):
      self.move_forward()
      cell = self.set_cell_value()
      cell.increment()
      self.change_cells(cell)

  def move_forward(self):
    while self.backtrack_index < len(self.solve_cells) -1 and self.solve_cells[self.backtrack_index].solved:
      self.backtrack_index += 1

  def set_cell_value(self):
    cell = self.solve_cells[self.backtrack_index]
    cell.set_value()
    return cell

  def change_cells(self,cell):
    if cell.is_valid_number():
      self.backtrack_index += 1
    else:
      self.decrement_cell(cell)

  def decrement_cell(self,cell):
    while cell.current_test_index == len(cell.potential_values) - 1:
      self.reset_cell(cell)
      self.backtrack()
      cell = self.solve_cells[self.backtrack_index]
    cell.current_test_index += 1

  def reset_cell(self,cell):
    cell.current_test_index = 0
    cell.value = 0
    self.board[cell.row][cell.col] = 0

  def backtrack(self):
    self.backtrack_index -= 1
    while self.solve_cells[self.backtrack_index].solved:
      self.backtrack_index -= 1
         
        
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

board = []
for i in range(9):
    board.append([int(i) for i in input()])
sudo = Sudoku(board)
sudo.solve()
print(sudo.__str__())


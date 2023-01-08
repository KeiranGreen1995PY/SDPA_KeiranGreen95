# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:05:40 2023

@author: judit
"""

### Part 1 SDPA Coursework (Dots & Boxes Game) Board Class

# This python file Board.py contains the board class for the text-based dots
# and boxes game
# This script creates a board class with a grid of dots and methods for 
# drawing the lines between the dots and checking to see if a player has
# completed a box.

class Board: #Create a class
    def __init__(self, rows, cols): #Intiate the attributes for the class Board
       self.rows = rows # Intiate the attribute row for the class Board
       self.cols = cols # Intiate the attribute cols fo the class Board
       self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
       
       def Draw_Line(self, row, col, horizontal):
           if horizontal:
               self.grid[row][col] +=1
           else:
               self.grid[row][col] =+2
               
    def Check_Box(self, row, col):
           if  self.grid[col][row] ==3:
                return True
           return False
       
    def Draw_Board(self):
        for row in self.grid: 
            print(" ".join(str(x) for x in row))
    
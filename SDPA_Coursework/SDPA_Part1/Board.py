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

class board: #Create a board class
    def __init__(self, rows, cols, players): #Intiate the attributes for the class Board
       self.rows = rows # Intiate the attribute row for the class Board
       self.cols = cols # Intiate the attribute cols for the class Board
       self.players = players #Intiate the attribute players for the class board
       self.grid = [[0 for _ in range(cols)] for _ in range(rows)] #Create nested list  to create a two dimensional list of 0s with rows number of the rows and cols number of the cols##
       self.player_positions = {player.name: (0, 0) for player in players} # Create a new dictionary
       
       def draw_Line(self, player, row, col, horizontal): #Method definition of class board
           if horizontal: #Check the value of the horizontal parameter
           else:
               self.grid[row][col] =+2 #Increment value at the speified row
               self.player_positions[player.name] = (row, col) #Update the value in self player positions#
               
    def check_Box(self, player, row, col):
           if  self.grid[col][row] ==3: ] # this code will run if col and row have a value of 3 
                return True #Return true if equal to 3
           return False #Return false if not equal to 3
       
    def Draw_Board(self):
        for row in self.grid: # a for loop that will iterate over a row in self grid 
            print(" ".join(str(x) for x in row)) #Create a new list of strings to each element in the row list converting non string element to a string. 
                                                  #Using Join concatenate the strongs in the list with the space 
            
            
    def get_player_positions(self):
        return self.player_positions #Return the value of self player positions
    
 

    
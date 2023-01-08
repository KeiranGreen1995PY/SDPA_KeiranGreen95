# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:19:06 2023

@author: judit
"""

### player.py: This python file contains classes for the Player and
### it's child classes (HumanPlayer, ComputerPlayer, SmartComputerPlayer)
### These classes get or generate a players move. 
# They make use of the Board class instance to validate and plot their move

from Board import Board # Import the board class to player class
import random

class Player:
    
    def __init__ (self, name, x, y, board): # Initialise the attributes of the class with the players name, starting location and board instance
        
        self.name = name #Create attribute of the class player which is name
        self.score = 0 #Create attribute of the class player which is score
        self.y = y #Create attribute of the class player which is Y
        self.x = x #Create attribute of the class player which is x
        self.board = board #Create attribute of the class player which is Board
       
    def add_point(self):
        self.score =+1
            
        #update the board with the initial positions
        self.board.update_board(self.name, self.score, self.x, self.y)
        
class ComputerPlayer(Player): # Adding a computer player class which inherits 
                              # from the player class and overrides the add_point method
                              # in order to make the computer player moves
    
    def add_point(self):
        self.score += 1
        row, col = self.get_random_move()
        horizontal = random.choice([True, False])
        self.board.draw_line(self, row, col, horizontal)
        self.board.update_board(self.name, self.score, row, col)
    def get_random_move(self):
        return random.randint(0, self.board.rows - 1)
        

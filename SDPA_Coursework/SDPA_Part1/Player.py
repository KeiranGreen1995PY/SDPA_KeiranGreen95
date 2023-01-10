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
    
    def add_point(self): #Method definition for the class player, and computer
        self.score += 1 #Increment the value of the score of the self object by 1
        row, col = self.get_random_move() #Call get random move method on the self object and assign the return value to the row and col#
        horizontal = random.choice([True, False]) #Assign random element to a list and assign it to the horizontal variable#
        self.board.draw_line(self, row, col, horizontal) #Call the draw line method from the board attribute of the self object and then pass it 4 arguments being self, row , col and horizontal#
        self.board.update_board(self.name, self.score, row, col) # Call the update board method from the board attribute of the self object and then pass it 4 arguments self name, self score , row and col.#
    def get_random_move(self):
        return random.randint(0, self.board.rows - 1) #create a random integer between 0 and self.board.rows - 1 using random module##
        

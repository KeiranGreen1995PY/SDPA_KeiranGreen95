# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:19:06 2023

@author: judit
"""

### player.py: This python file contains classes for the Player and
### it's child classes (HumanPlayer, ComputerPlayer, SmartComputerPlayer)
### These classes get or generate a players move. 
# They make use of the Board class instance to validate and plot their move

from Board import board # Import the board class to player class

class Player:
    def __init__ (self, name, x, y, Board): # Initialise the attributes of the class with the players name, starting location and board instance
        """ initialise the Player instance with the players name, start position and board instance.

		parameters:
		name - player name. Used a the players board character
		x- player start row position on the board
		y - player start column position on the board
		board - instance of the board class. This will be used to invoke Board methods

		return the initialized Player instance """
		
        self.name = name #represent instance name of the player class
        self.y = y #represent instance y of the player class
        self.x = x #represent instance x of the player class
        self.board = board #represent instance board of the player class
        #update the board with the initial positions
        self.board.update_board(self.name, self.x, self.y)
        
    def move(self, direction):
        """ Validate the player direction and use the board instance to validate the move target.

		parameters:
		direction - direction of the player's move

		returns:
		the move target validation result - True for non-suicidal move, False for a move resulting in the end of the game
		the validation result information message """        
		# store potential new position (not validated yet)
        
        
		



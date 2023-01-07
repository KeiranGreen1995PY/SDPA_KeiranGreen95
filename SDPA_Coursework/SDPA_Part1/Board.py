# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:05:40 2023

@author: judit
"""

### Part 1 SDPA Coursework (Dots & Boxes Game) Board Class

### This python file Board.py contains the board class for the text-based dots and boxes game

class Board:
    """ Confirm the player move, plot the player paths and then print the board #

        Determine if any of the players have won the game, lost the game or if it has resulted in 
        a draw (drawn in simultaneous mode).
        In the simultaneous mode, the board is only shown after both players have moved"""

    def __init__(self, size):
        """ Configure the Board instance with size, name, game mode, and option.

		Parameters:
		size - the size of the board game in length (the board is a square)

		returns the confirmed board instance """

        self.size = size
        self.grid = [[" " for i in range(size)] for j in range(size)]
    
     #print the board game, overwrite the __str__ function which is built in
    def __str__(self):
        
        """ print the Board class instance current state but using the board grids variable. """
        k=""
        
        k+="-" * (self.size * 2 + 1)+"\n"
        
        for row in self.grid:
            
            k+="|" + ("|".join(str(x) for x in row) + "|")+"\n"  
            
        k+="-" * (self.size * 2 + 1)+"\n"
        
        return k

    def update_board(self, value, x, y):
        """ place the line or player on the board game.

		parameters:
		value - the current player, which could be the players new position or the players line
		x - Row location on the board game to place the player
		y - Column position on the board to place the player """


    def is_valid_move(self, player_name, target_row, target_col):
        """ validate the current player's move.

        A valid move will cause the board being re-printed
        In simultaneous mode, print the board but only if both of the players have chosen to move

		parameters:
        target_row1 - Players row position located on the board
        target_col1 - Players column location on the board
        Players_name - Players name
		
		
		returns:
		the validation result - It is True for a valid move, and it is False for an invalid move
		 """
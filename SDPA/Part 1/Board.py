# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:05:40 2023

@author: judit
"""

# Part 1 SDPA Coursework (Dots & Boxes Game)

# This python file Board.py contains the board class for the text-based dots and boxes game

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
        s=""
        
        s+="-" * (self.size * 2 + 1)+"\n"
        
        for row in self.grid:
            
            s+="|" + ("|".join(str(x) for x in row) + "|")+"\n"  
            
        s+="-" * (self.size * 2 + 1)+"\n"
        
        return s

    
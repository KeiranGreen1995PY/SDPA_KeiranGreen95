# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:19:04 2023

@author: judit
"""
### Part 1 SDPA Coursework (Dots & Boxes Game) Main Script
# Main.py:	This python script file will run the implemented Board and Player classes
### It will run the dots and boxes game and import the Board and player classes
# which imports and also makes use of the Board and Player classes. 
# It will present the game menu which allows for various game options.

from Board import Board # Imports the Board classes
from Player import Player # Imports the Player classes


while (True): # Creates a loop for the dots & boxes main game menu

	
    while True: # Board size input & validation loop
        try:
			# From the user input this captures the board size for the game 
            boardgame_size = int(input ("Input board size (greater than 3): "))
            if boardgame_size <= 3:
                print ("Board size must be bigger than 3")
            else:
				# break out of the board size input and validation loop
                break
        except ValueError:
            print("Please enter a valid number.")
		
		# return to the board size input and validation loop
   
    # initialise the board instance with the size
    dots_boxes_board = Board(boardgame_size)
    
    #create two objects of the player class
    # set the starting position for the players  (this can be an input too)
    player1 = Player ("1", 0, 0, dots_boxes_board)
        
    # set the starting position for the player two at the right bottom corner 
    player2 = Player ("2", boardgame_size - 1, boardgame_size - 1, dots_boxes_board)
    
    # print the board game start state with the 2 players in their initial positions
    print(dots_boxes_board)

    # game play loop
    valid_move= True
    while(valid_move):
        for Player in [player1, player2]:
           # Get the player's move from the user
           move= ""
           while move not in ["l","r","u", "d"]: 
                 move = input(f'{Player.name} - enter your move (u, d, l, r): ')
           valid_move= Player.move(move)
           if valid_move == False:
                break
   
    
   # Break if not playing again
    play_again = input ("Would you like to pay again? (y or n): ")
    if(play_again.lower()!='y' and play_again.lower()!='yes' ): 
        print ("Thanks for playing, end of the game")
        break
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

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

player1 = Player(input("Enter the name for player1: "))
player2 = Player(input("Enter the name for player2: "))

Current_player = 0
while true:
        
    print(f{"players[Current_player].name}'s turn")
    row = int(input("Enter the row: "))
    col = int(input("Enter the column: "))
    horizontal = input("Enter H for the Horizontal line, V for vertical:").upper() == "H"
        
    board.draw_line(row, col, horizontal)
    board.draw_board()
if  board.check_box(row, col):
    player[Current_player].add_point()
    print(f"{players[Current_player].name} will receive a point!")
    Current_player = (Current_player + 1) % 2
        
if __name__ == "__main__":
    main()
        
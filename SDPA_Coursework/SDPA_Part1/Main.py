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

from Board import Board # Imports the Board class
from Player import Player # Imports the Player class
from ComputerPlayer import ComputerPlayer # Imports the ComputerPlayer Class

def main(): 

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    board = Board(rows, cols) # Created a board object

    player1 = Player(input("Enter the name for player1: "))
    player2 = Player(input("Enter the name for player2: "))
    players = [player1, player2] # Created a list for the players
    
    Current_player = 0
    while True:
        
        print(f"{players[Current_player].name}'s turn")
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        horizontal = input("Enter H for the Horizontal line, V for vertical: ").upper() == "H"
        
        if not board.draw_line(player1, row1, col1, horizontal1)
        print("Thats not a valid movement, please try that again")
        continue
        row2, col2, horizontal2 = player2.get_random_move()
        if not board.draw_line(player2, row2, col2, horiontal2):
        print("Thats not a valid movement , please try that again")
        continue
        if row1 == row2 and col1 == col2 and horizontal1 == horizontal2:
            if board.check_box(player1, row1, col1):
                player1.add_point()
                player2.add_point()
                print(f"{player1.name} and {player2.name} will receive a point, they have completed a box")
            else:
                print("There was a confliction, enter different moves")
                continue
            
            board.draw_board()
        if board.check_box(row, col):
        print(f"{player.name} has completed a box")
        player[Current_player].add_point()
        print(f"{players[Current_player].name} will receive a point!")
        Current_player = (Current_player + 1) % 2
        if all(player.score == rows * cols for player in board.players):
            print("Game is over")
            if player1.score > player2.score:
            print(f"{player.name} wins")
        elif player2.score > player1.score:
            print(f"{player.name} wins")
        else:
            print("Its a draw and nobody wins")
            break
        
if __name__ == "__main__":
    main()
        
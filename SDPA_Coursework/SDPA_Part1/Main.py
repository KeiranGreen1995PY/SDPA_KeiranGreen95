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

def main(): # Starting point of the Dots & Boxes Programme

    rows = int(input("Enter the number of rows: ")) #Take input from the player on rows
    cols = int(input("Enter the number of columns: ")) # Take input from the player on columns
    
    board = Board(rows, cols) # Created a board object

    player1 = Player(input("Enter the name for player1: ")) #Take input on players name for player 1
    player2 = Player(input("Enter the name for player2: ")) #Take input on players name for player 2
    players = [player1, player2] # Creat a new list for the players
    
    Current_player = 0 
    while True: # Create a while true loop until break statement executes within the loop
        
        print(f"{players[Current_player].name}'s turn")
        row = int(input("Enter the row: ")) #Take input for row
        col = int(input("Enter the column: ")) #Take input for column
        horizontal = input("Enter H for the Horizontal line, V for vertical: ").upper() == "H" #Take input for the horizontal line
        
        if not board.draw_line(player1, row1, col1, horizontal1) #If draw line method of the board object returns true, if not print the message and continue
        print("Thats not a valid movement, please try that again")
        continue
        row2, col2, horizontal2 = player2.get_random_move()
        if not board.draw_line(player2, row2, col2, horiontal2): #If draw line method of the board object returns true, if not print the message and continue
        print("Thats not a valid movement , please try that again")
        continue
        if row1 == row2 and col1 == col2 and horizontal1 == horizontal2: # Check if row 1 , row 2 are equal, check if col 1, col 2 are equal and check if horizontal 1 and 2 are equal
            if board.check_box(player1, row1, col1): #Check if the check box method of the board object is when called with player 1 , row 1 and col 1
                player1.add_point()
                player2.add_point()
                print(f"{player1.name} and {player2.name} will receive a point, they have completed a box")
            else:
                print("There was a confliction, enter different moves")
                continue
            
            board.draw_board()
        if board.check_box(row, col):
        print(f"{player.name} has completed a box") # Check if check box method of the board object returns true when it is called with row and col, if returns true the code in the if block will run
        player[Current_player].add_point()
        print(f"{players[Current_player].name} will receive a point!") # Will call the add point method on the object player with the current_player attribute, by which it will add a point to the players score
        Current_player = (Current_player + 1) % 2 #Updates the value of current player by adding the value 1 and taking the remainder of the result  when divided by 2, this causes current player to alternate between 0 and 1 when the code is run
        if all(player.score == rows * cols for player in board.players):
            print("Game is over") #Check if all the players have reached the maximum score equal to the number of rows multiplied by the number of columns
            if player1.score > player2.score: #Check if the player 1 score is greater than player 2 score. 
            print(f"{player.name} wins") #If true this message will print
        elif player2.score > player1.score: #Checks if player 2 score is greater than player 1 score
            print(f"{player.name} wins") #If true this message will then be printed
        else: #If the statements above  is false 
            print("Its a draw and nobody wins") #This message will be printed and the game will be a draw
            break
        
if __name__ == "__main__": # Checks if name variable is equal to string main 
    main() 
        
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:05:40 2023

@author: judit
"""

### Part 1 SDPA Coursework (Dots & Boxes Game) Board Class

### This python file Board.py contains the board class for the text-based dots and boxes game

class Board:
    def __init__(self, size):
       self.size = size
       self.grid = [[" " for i in range(size)] for j in range(size)]
    
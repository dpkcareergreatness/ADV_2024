#!/usr/bin/python

import pdb

grid = []

def ParseInput():
    with open("./day4.txt") as f:
        for line in f:
            line = line.strip("\n")
            grid.append(line)

def count_xmas_occurrences(grid, word="XMAS"):
    rows = len(grid)  # Number of rows in the grid
    cols = len(grid[0])  # Number of columns in the grid
    word_len = len(word)  # Length of the word "XMAS"
    
    # Define the possible directions
    directions = [
        (0, 1), (0, -1),  # Horizontal: right and left
        (1, 0), (-1, 0),  # Vertical: down and up
        (1, 1), (-1, -1), # Diagonal: down-right and up-left
        (1, -1), (-1, 1)  # Diagonal: down-left and up-right
    ]
    
    # Function to check if a position is within the grid boundaries
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    # Function to check if the word "XMAS" can be formed starting from (x, y) in direction (dx, dy)
    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy  # Calculate the next position
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False  # Return False if out of bounds or character doesn't match
        return True  # Return True if the word "XMAS" is found
    
    count = 0  # Initialize the count of occurrences
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if search_from(r, c, dx, dy):
                    count += 1  # Increment the count if the word "XMAS" is found
    
    return count

ParseInput()
print(count_xmas_occurrences(grid))
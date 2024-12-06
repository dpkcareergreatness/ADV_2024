#!/usr/bin/python

import pdb

grid = []

def ParseInput():
    with open("./day4.txt") as f:
        for line in f:
            line = line.strip("\n")
            grid.append(line)

def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search_xmas(x, y):
        count = 0
        if grid[x][y] == 'A':
            for dx1, dy1 in [(1, 1), (-1, -1)]:
                for dx2, dy2 in [(1, -1), (-1, 1)]:
                    if is_valid(x + dx1, y + dy1) and is_valid(x + dx2, y + dy2) and \
                       is_valid(x - dx1, y - dy1) and is_valid(x - dx2, y - dy2):
                        if grid[x + dx1][y + dy1] == 'M' and grid[x + dx2][y + dy2] == 'S' and \
                           grid[x - dx1][y - dy1] == 'S' and grid[x - dx2][y - dy2] == 'M':
                            count += 1
        return count
    
    total_count = 0
    for r in range(rows):
        for c in range(cols):
            total_count += search_xmas(r, c)
    
    return total_count

ParseInput()
print(count_xmas_patterns(grid))
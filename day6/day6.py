#!/usr/bin/python
import pdb

d = {}
grid = []
gridWidth = 0
gridHeigth = 0

#guard states
guardState = None
guardXPos = 0
guardYPos = 0
guardUniquePathTraversed = 1
#Guard current State: nextStep x,y
nextMove = {ord('^') : [0, -1],
			ord('>') : [1, 0],
			ord('v') : [0, 1],
			ord('<') : [-1, 0]}
#Guard next move on obstacle
guardNextState =  {ord('^') : ord('>'),
				   ord('>') : ord('v'),
				   ord('v') : ord('<'),
				   ord('<') : ord('^')}

def IsOutsideGrid(x, y, gridWidth, gridHeight):
    return x < 0 or y < 0 or x >= gridWidth or y >= gridHeight

def traverseGrid(grid, gridWidth, gridHeight, guardState, guardXPos, guardYPos):
    global nextMove
    (xInc, yInc) = nextMove[guardState]
    uniquePathTraversed = 0
    while True:
        XPos = guardXPos + xInc
        YPos = guardYPos + yInc
        if IsOutsideGrid(XPos, YPos, gridWidth, gridHeight):
            return [uniquePathTraversed, -1, -1]
        elif grid[YPos][XPos] == ord(".") or grid[YPos][XPos] == ord("X"):
            guardXPos = XPos
            guardYPos = YPos
            if grid[YPos][XPos] == ord("."):
                uniquePathTraversed += 1
                grid[YPos][XPos] = ord("X")
        elif grid[YPos][XPos] == ord("#"):
            break
    return [uniquePathTraversed, guardXPos, guardYPos]

def ParseInput():
    global guardState, guardXPos, guardYPos, gridWidth, gridHeight
    with open("./s.txt") as f:
        for line in f:
            line = line.strip("\n")
            temp = []
            xPos = 0
            for ch in line:
                num = ord(ch)
                if ((num == ord('^')) or (num == ord('>')) or (num == ord('v')) or (num == ord('<'))):
                    guardState = num
                    guardXPos = xPos
                    num = ord("X")
                temp.append(num)
                xPos += 1

            grid.append(temp)
            if guardState == None:
                guardYPos += 1

        gridWidth = len(grid[0])
        gridHeight = len(grid)
        print(grid, gridWidth, gridHeight)

ParseInput()

while True:
    print(f"Guard Position: ({guardXPos}, {guardYPos}), State: {chr(guardState)}")
    [uniquePathTraversed, XPos, YPos] = traverseGrid(grid, gridWidth, gridHeight, guardState, guardXPos, guardYPos)
    guardUniquePathTraversed += uniquePathTraversed
    if XPos == -1 or YPos == -1:
        print("Unique path traversed is count", guardUniquePathTraversed)
        break
    else:
        guardXPos = XPos
        guardYPos = YPos
        guardState = guardNextState[guardState]
    print(f"Updated Guard Position: ({guardXPos}, {guardYPos}), State: {chr(guardState)}")
    print("Grid:")
    for row in grid:
        print("".join(chr(c) for c in row))

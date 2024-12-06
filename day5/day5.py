#!/usr/bin/python

import pdb

pageOrdering = {}
bUpdatePageOrdering = True
safeUpdateMidPageSum = 0

def IsUpdateValid(pu):
    
    #Iterate through the page update line
    #Next, Iterate the pageOrdering for the particular page. If any of the dependent pages is marked as updated, its not a valid update
    #Maintain another dictionary to mark page as updated
    pagesWritten = {}
    for page in pu:
        dependentPages = pageOrdering.get(page, None)
        if dependentPages != None:
            for depPage in dependentPages:
                if pagesWritten.get(depPage, -1) != -1:
                    return False
        #Mark the page as written
        pagesWritten[page] = 1   
    print ("Safe Update ", pu)    
    
    return True

def ParseInput():
    global bUpdatePageOrdering, safeUpdateMidPageSum
    with open("./day5.txt") as f:
        for line in f:
            pageUpdate = []
            line = line.strip("\n")
            if line == "":
                print("Line break")
                bUpdatePageOrdering = False
                continue
            
            if bUpdatePageOrdering == True:
                num1, num2 = line.split("|")
                num1 = int(num1)
                num2 = int(num2)
                if (pageOrdering.get(num1, -1) == -1):
                    pageOrdering[num1] = [num2]
                else:
                    pageOrdering[num1].append(num2)
            else:
                temp = (line.split(","))
                for ch in temp:
                    pageUpdate.append(int(ch))

                if (IsUpdateValid(pageUpdate) == True):
                    length = len(pageUpdate)
                    safeUpdateMidPageSum = safeUpdateMidPageSum + pageUpdate[length//2]

ParseInput()
print("Answer is ", safeUpdateMidPageSum)

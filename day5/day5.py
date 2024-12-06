#!/usr/bin/python

import pdb

pageOrdering = {}
bUpdatePageOrdering = True
safeUpdateMidPageSum = 0
fixedUpdateMidPageSum = 0

def FixIncorrectUpdates(pu):
    fixedList = [0 for _ in range(len(pu))]
    #Iterate page by page
    for page in pu:
        newOffset = 0
         #For each page, if it is in the dependency list of other pages, increment its index in the new list by 1
        for p in pu:
            depPage = pageOrdering.get(p, None)
            if depPage != None:
                if page in depPage:
                    newOffset = newOffset + 1
        fixedList[newOffset] = page

    return fixedList

def IsUpdateValid(pu):
    
    #Iterate through the page update line
    #Next, Iterate the pageOrdering for the particular page. If any of the dependent pages is marked as updated, its not a valid update
    #Maintain another dictionary to mark page as updated
    pagesWritten = {}
    bUpdateValid = True
    for page in pu:
        dependentPages = pageOrdering.get(page, None)
        if dependentPages != None:
            for depPage in dependentPages:
                if pagesWritten.get(depPage, -1) != -1:
                    bUpdateValid = False
                    return bUpdateValid
        #Mark the page as written
        pagesWritten[page] = 1   
    print ("Safe Update ", pu)    

    return bUpdateValid

def ParseInput():
    global bUpdatePageOrdering, safeUpdateMidPageSum, fixedUpdateMidPageSum
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

                output = IsUpdateValid(pageUpdate)
                if (output == True):
                    length = len(pageUpdate)
                    safeUpdateMidPageSum = safeUpdateMidPageSum + pageUpdate[length//2]
                else:
                    fixedList = FixIncorrectUpdates(pageUpdate)
                    output = IsUpdateValid(fixedList)
                    print("Fixed list is ", fixedList)
                    length = len(fixedList)
                    fixedUpdateMidPageSum = fixedUpdateMidPageSum + fixedList[length//2]

ParseInput()
print("Answer part1 is ", safeUpdateMidPageSum)
print("Answer part2 is ", fixedUpdateMidPageSum)

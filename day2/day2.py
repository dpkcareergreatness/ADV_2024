#!/usr/bin/python
import pdb

globalList = []
safeCount = 0

def ParseInput():
	with open("day2.txt") as f:
		for line in f:
			line = line.strip("\n")
			list =  [int(l) for l in line.split(" ")]
			globalList.append(list)

def _SafetListChecker(list, bCheckDecreasing):
	prev = None
	for num in list:
		if prev != None:
			if bCheckDecreasing == False:
				#Should be strictly increasing
				if prev >= num:
					return False
			else:
				#Should be strictly decreasing
				if num >= prev:
					return False
			
			if abs(prev - num) > 3:
				return False

		prev = num
	
	return True


def IsSafe():
	global safeCount
	bSafe = None

	for list in globalList:
		for index in range(len(list)):
			newList = list[0:index] + list[index+1::]
			bSafe = _SafetListChecker(newList, False) or _SafetListChecker(newList, True)
			if bSafe == True:
				print ("Safe list", list)
				safeCount = safeCount+1
				break

	return bSafe


ParseInput()

IsSafe()

print("Safe count is ", safeCount)
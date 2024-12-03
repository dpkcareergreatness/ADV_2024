#!/usr/bin/python

d = {}
list1 = []
count = 0

def ParseInput():
	with open("../day1.txt") as f:
		for line in f:
			line = line.strip("\n")
			[num1, num2] = line.split("   ")
			num1 = int(num1)
			num2 = int(num2)
			list1.append(num1)
			if d.get(num2, -1) == -1:
				d[num2] = 1
			else:
				d[num2] = d[num2] + 1

def GetSimilarityScore():
	global count
	for num in list1:
		if d.get(num, -1) != -1:
			count = count + (num * d[num])
	
	return count


ParseInput()
similarityScore = GetSimilarityScore()
print("Similarity score is %{}", similarityScore)

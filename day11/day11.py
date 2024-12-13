#!/usr/bin/python
import pdb
def ParseInput(fileName):
	nums = []
	with open(fileName) as f:
		for line in f:
			line = line.strip("\n")
			list = line.split(" ")
			nums = [int(num) for num in list]
	return (nums)

def TransformNumbers(nums, blinkCount):
	trnaformedNums = []
	for _ in range(blinkCount):
		if trnaformedNums:
			nums = trnaformedNums
			trnaformedNums = []
			#pdb.set_trace()

		for num in nums:
			if num == 0:
				trnaformedNums.append(1)
			elif (len(str(num)) % 2) == 0:
				splitAtIndex = len(str(num)) // 2
				temp = str(num)
				#pdb.set_trace()
				str1 = temp[0:splitAtIndex]
				str2 = temp[splitAtIndex::]
				trnaformedNums.append(int(str1))
				trnaformedNums.append(int(str2))
			else:
				num = num * 2024
				trnaformedNums.append(num)
		#print(trnaformedNums)

	return trnaformedNums

nums = ParseInput("./day11.txt")
blinkCount = 25
transformedNums = TransformNumbers(nums, blinkCount)
#print(transformedNums)

print("Answer part1 is ", len(transformedNums))
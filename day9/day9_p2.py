#!/usr/bin/python
import pdb
diskMap = {}

def ParseInput():
	global diskMap
	with open("./day9.txt") as f:
		for line in f:
			idx = 0
			id = 0
			while (idx < len(line)):
				ch1 = (line[idx])
				#Sometimes there are no free space in the disk
				if (idx + 1 < len(line)):
					ch2 = (line[idx + 1])
				else:
					ch2 = '0'
				#print (ch1, ch2)
				diskMap[id] = (ch1, ch2, False)
				idx = idx + 2
				id = id + 1

def QueryMovableFile(tailIndex, stopAtFileIndex, maxFreeBlocksCount):
	retIndex = None
	while (tailIndex > stopAtFileIndex):
		fileBlocksCount, _, fileMoved = diskMap[tailIndex]
		fileBlocksCount = int(fileBlocksCount)
		if ((fileMoved == True) or (fileBlocksCount > maxFreeBlocksCount)):
			#Can't fit this file ID here. Skip
			tailIndex = tailIndex - 1
		else:
			#found file suitable to fit in the space, return the file ID
			retIndex = tailIndex
			break
	
	return retIndex


#Output: String of the memory
#Tricky part is that the id might be more than 1 digit so we cant do without () else id=10 would be trated as 1 and 0 in checksum instead of 10
def CompactMemory():
	global diskMap
	id = 0
	lastId = -1
	outputString = ''
	while (id < (len(diskMap))):
		tailIndex = len(diskMap) - 1
		fileBlocksCount, freeBlocksCount, fileMoved = diskMap[id]
		fileBlocksCount = int(fileBlocksCount)
		freeBlocksCount = int(freeBlocksCount)
		if id != lastId:
			if fileMoved == False:
				outputString = outputString + ('('+str(id)+')') * fileBlocksCount
			else:
				outputString = outputString + ('('+str(0)+')') * fileBlocksCount
			lastId = id

		#File blocks to remap
		tailIndex = QueryMovableFile(tailIndex, id, freeBlocksCount)
		#pdb.set_trace()
		if tailIndex == None:
			#Nothing fits the available space for this id, so we leave it empty marking it as (0) so that it doesnt account for CRC
			outputString = outputString + ('('+str(0)+')') * freeBlocksCount
			id = id + 1
		#Enough free blocks to relocate file in full
		else:
			remappedFileBlocksCount,tailIndexFreeBlocks,fileRemappedStatus = diskMap[tailIndex]
			remappedFileBlocksCount = int(remappedFileBlocksCount)
			outputString = outputString + ('('+str(tailIndex)+')') * remappedFileBlocksCount
			diskMap[id] = (str(fileBlocksCount) , str(freeBlocksCount - remappedFileBlocksCount), False)
			diskMap[tailIndex] = (remappedFileBlocksCount ,tailIndexFreeBlocks, True)
			if (freeBlocksCount - remappedFileBlocksCount) == 0:
				id = id + 1

	return outputString

def ComputeCheckSum(memString):
	checkSum = 0
	bNumStart = False
	id = 0
	for c in memString:
		if c == '(':
			bNumStart = True
			num = 0
			continue
		elif c == ')':
			bNumStart = False
			checkSum = checkSum + id * num
			id = id + 1
		elif bNumStart == True:
			num = num * 10 + int(c)
	
	return checkSum


ParseInput()
#print (diskMap, len(diskMap))
#pdb.set_trace()
memoryString = CompactMemory()
#pdb.set_trace()
#print(memoryString)

chkSum = ComputeCheckSum(memoryString)
print("Answer part 2 is ", chkSum)

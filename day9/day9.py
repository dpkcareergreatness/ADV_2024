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
				diskMap[id] = (ch1, ch2)
				idx = idx + 2
				id = id + 1

#Output: String of the memory
#Tricky part is that the id might be more than 1 digit so we cant do without () else id=10 would be trated as 1 and 0 in checksum instead of 10
def CompactMemory():
	global diskMap
	outputString = ''
	tailIndex = len(diskMap) - 1
	id = 0
	lastId = -1
	while (id < (len(diskMap))):
		fileBlocksCount, freeBlocksCount = diskMap[id]
		fileBlocksCount = int(fileBlocksCount)
		freeBlocksCount = int(freeBlocksCount)
		if id != lastId:
			outputString = outputString + ('('+str(id)+')') * fileBlocksCount
			lastId = id

		#File blocks to remap
		remappedFileBlocksCount,tailIndexFreeBlocks = diskMap[tailIndex]
		remappedFileBlocksCount = int(remappedFileBlocksCount)
		#pdb.set_trace()
		if id == tailIndex:
			break

		#Enough free blocks to relocate file in full
		if freeBlocksCount >= remappedFileBlocksCount:
			outputString = outputString + ('('+str(tailIndex)+')') * remappedFileBlocksCount
			diskMap[id] = (str(fileBlocksCount) , str(freeBlocksCount - remappedFileBlocksCount))
			diskMap[tailIndex] = ('0' ,tailIndexFreeBlocks)
			#Move tail pointer to next index
			tailIndex = tailIndex - 1
		else:
			#Not enough memory to relocate tail Index completely
			outputString = outputString + ('('+str(tailIndex)+')') * freeBlocksCount
			diskMap[id] = (str(fileBlocksCount) ,'0')
			reaminingTailFileBlockCount = remappedFileBlocksCount - freeBlocksCount
			diskMap[tailIndex] = (str(reaminingTailFileBlockCount) ,tailIndexFreeBlocks)
			#Move front id to next index
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
memoryString = CompactMemory()
#pdb.set_trace()
#print(memoryString)

chkSum = ComputeCheckSum(memoryString)
print("Answer part 1 is ", chkSum)

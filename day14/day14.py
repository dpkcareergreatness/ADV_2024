#!/usr/bin/python
guards = []
import pdb

class PatrolRoom:
	def __init__(self, width, height):
		self.Width = width
		self.height = height
		self.guardsQuad1 = 0
		self.guardsQuad2 = 0
		self.guardsQuad3 = 0
		self.guardsQuad4 = 0

	def GetRoomHeight(self):
		return self.height
	
	def GetRoomWidth(self):
		return self.Width
	
	def UpdateGuards(self, guardXPos, guardYPos):
		quad1XPos = (self.Width // 2) - 1
		quad1YPos = (self.height // 2) - 1

		quad2XPos = (self.Width - 1)
		quad2YPos = (self.height // 2) - 1

		quad3XPos = (self.Width // 2) - 1
		quad3YPos = self.height - 1

		quad4XPos = (self.Width - 1)
		quad4YPos = self.height - 1

		if (guardXPos < 0):
			guardXPos = self.Width + (guardXPos)
		if (guardYPos < 0):
			guardYPos = self.height + (guardYPos)

		guardXPos %= self.Width
		guardYPos %= self.height

		print("Guard positions for update: x,y",guardXPos, guardYPos)
		#if (guardXPos == 6) or (guardXPos == 9):
			#pdb.set_trace()
		if (guardXPos == self.Width // 2) or (guardYPos == self.height // 2):
			return
		if (guardXPos < 0) or (guardYPos < 0):
			return
		if (guardXPos >= 0) and (guardXPos <= quad1XPos) and (guardYPos >= 0) and (guardYPos <= quad1YPos):
			self.guardsQuad1 += 1
		elif (guardXPos > quad1XPos) and (guardXPos <= quad2XPos) and (guardYPos >= 0) and (guardYPos <= quad2YPos):
			self.guardsQuad2 += 1
		elif (guardXPos >= 0) and (guardXPos <= quad3XPos) and (guardYPos >= quad2YPos) and (guardYPos <= quad3YPos):
			self.guardsQuad3 += 1
		elif (guardXPos > quad3XPos) and (guardXPos <= quad4XPos) and (guardYPos >= quad2YPos) and (guardYPos <= quad4YPos):
			self.guardsQuad4 += 1

	def GetSafetyScore(self):
		print("Guards in quad are ", self.guardsQuad1, self.guardsQuad2, self.guardsQuad3, self.guardsQuad4)
		return self.guardsQuad1 * self.guardsQuad2 * self.guardsQuad3 * self.guardsQuad4

class Guard:
	def __init__(self, x,y,velX,velY):
		self.x = x
		self.y = y
		self.velX = velX
		self.veY = velY

	def SimulatePosition(self, timeInSeconds, roomWidth, roomHeight):
		self.x = (self.x + self.velX * timeInSeconds) % roomWidth
		self.y = (self.y + self.veY * timeInSeconds) % roomHeight
	
	def PrintGuards(self):
		print("x , y, velX, velY ", self.x, self.y, self.velX, self.veY)
	
	def GetGuardsXPos(self):
		return self.x
	
	def GetGuardsYPos(self):
		return self.y


def ParseInput(fileName):
	global guards
	with open(fileName) as f:
		for line in f:
			line = line.strip("\n")
			temp1, temp2 = line.split(" ")
			_,coords = temp1.split("=")
			x,y = coords.split(",")
			#print(x,y)
			_,temp = temp2.split("=")
			velX, velY = temp.split(",")
			x = int(x)
			y = int(y)
			velX = int(velX)
			velY = int(velY)
			guards.append(Guard(x,y,velX,velY))


def main():
	ParseInput("./day14.txt")
	roomWidth = 101
	roomHeight = 103
	timeInSecods = 100
	patrolRoom = PatrolRoom(roomWidth, roomHeight)
	for id, guard in enumerate(guards):
		#print(id)
		#guard.PrintGuards()
		guard.SimulatePosition(timeInSecods, roomWidth, roomHeight)
		patrolRoom.UpdateGuards(guard.GetGuardsXPos(), guard.GetGuardsYPos())
	safetyScore = patrolRoom.GetSafetyScore()
	print("Answer part1 is ", safetyScore)

if __name__ == '__main__':
	main()
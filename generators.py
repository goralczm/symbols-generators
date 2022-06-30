import random
import math
from turtle import distance

def CalculateDistance(pointA, pointB):
	return int(math.sqrt((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2))

def OneSidePyramid(height, inverse=False, symbol='#'):
	heightRange = range(1, height+1)
	if (inverse):
		heightRange = heightRange[::-1] #Inverse loop
	for row in heightRange:
		rowContent = ''
		for column in range(row):
			rowContent += symbol
		print(rowContent)

def PyramidBasedWidth(width, symbol='#', background=' '):
	rowContent = ''
	finalRow = symbol*width
	rowIndex = 1
	while(rowContent != finalRow):
		if (width % 2 != 0):
			whiteSpaces = background*((width//2)-rowIndex//2)
			branches = symbol*rowIndex
			rowIndex += 2
		else:
			whiteSpaces = background*((width-(rowIndex*2))//2)
			branches = symbol*2*rowIndex
			rowIndex += 1
		rowContent = whiteSpaces+branches+whiteSpaces
		print(rowContent)
			
def PyramidBasedHeight(height, inverse=False, symbol='#', background=' '):
	rowContent = ''
	width = 2 * (height - 1) + 1
	rowIndex = 1
	heightRange = range(1, height + 1)
	if inverse:
		heightRange = heightRange[::-1]
		rowIndex = width
	for columnIndex in heightRange:
		whiteSpaces = background * ((width // 2) - rowIndex // 2)
		branches = symbol*rowIndex
		rowContent = whiteSpaces+branches+whiteSpaces	
		rowIndex = (rowIndex + 2) if not inverse else (rowIndex - 2)
		print(rowContent)

def BlackHole(width, height, density=4, tolerance=4, rejection=0, mode='diamond', offset=[0, 0], symbol='#', background=' ', secondarySymbol=''):
	with open('black_hole.txt', 'w') as file:
		center = [width//2, height//2]
		for row in range(width):
			rowContent = ''
			for column in range(height):
				columnIndex = column if column <= center[0] else width - 1 - column
				if ('diamond' in mode):
					rowIndex = row if row <= center[1] else height - 1 - row
					distanceFromCenter = abs((min(width, height)) - 1 - columnIndex - rowIndex)
				elif ('circle' in mode):
					location = [row, column]
					distanceFromCenter = CalculateDistance(location, [center[0] + offset[1], center[1] - offset[0]])
				if ('matrix' in mode):
					rowContent += ' ' + str(distanceFromCenter)
					continue

				randomIndex = random.randint(0, distanceFromCenter) #Determines if 'pixel' should be instantiated
				minValToCreate = (min(width, height)) // 16 * density
				minDistance = min(width, height) // 8 * tolerance
				if (randomIndex <= minValToCreate):
					if (distanceFromCenter < minDistance):
						if (rejection > 0):
							maxRejectionValue = 100 // (10 * rejection) // ((distanceFromCenter + 5) // 4)
							randomRejectionValue = (random.randint(0, maxRejectionValue))
							if (randomRejectionValue != maxRejectionValue):
								rowContent += ' ' + symbol
							else:
								rowContent += ' ' + secondarySymbol
						else:
							rowContent += ' ' + symbol
					else:
						rowContent += ' ' + secondarySymbol
				else:
					rowContent += ' ' + background
			file.write(rowContent+'\n')

def Tree(gridSize, density=4, tolerance=4, rejection=0, mode='diamond', symbol='#', background=' '):
	with open('tree.txt', 'w') as file:
		center = [gridSize//2, gridSize//2]
		for row in range(gridSize):
			rowContent = ''
			for column in range(gridSize):
				columnIndex = column if column <= center[0] else gridSize - 1 - column
				if (mode == 'diamond'):
					rowIndex = row if row <= center[0] else gridSize - 1 - row
					distanceFromCenter = abs(gridSize - 1 - columnIndex - rowIndex)
				elif (mode == 'circle'):
					coords = [row, column]
					distanceFromCenter = CalculateDistance(coords, center)
				randomIndex = random.randint(0, distanceFromCenter)
				if ((randomIndex <= (gridSize)//16*density and distanceFromCenter < gridSize // 8 * tolerance) or (row > center[0] and columnIndex > center[0]//1.2)):
					if (rejection > 0):
						rejectionRate = 100//(10*rejection)
						if ((random.randint(0, rejectionRate)) != rejectionRate):
							rowContent += ' '+symbol
						else:
							rowContent += ' '+background
					else:
						rowContent += ' '+symbol
				else:
					rowContent += ' '+background
			file.write(rowContent+'\n')

BlackHole(128, 128, 1.5, 2, 2, 'circle', [0, 0], '#', ' ', '.')
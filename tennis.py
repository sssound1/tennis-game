file1 = open('full_tournament.txt', 'r');
Lines = file1.readlines()
Lines.append("\nM")

pointArrays = [] # [[0,1,1],[1,1,0,0],..]
gameArrays = [] # [[23, 17], [1, 1], ..]
playerArrays = [] # [[A,C], [A,B], ...]

def calculateGames(pointArray):
	print("hey")

pointArray = []

for line in Lines:
	if line.strip() == "":
		continue
	if line.strip()[0] == 'M':
		if len(pointArray) > 0 : 
			calculateGames(pointArray)
			pointArrays.append(pointArray)
		pointArray = []
	elif line.strip()[0] == 'P':
		playerArray = [line.strip().split(' ')[1],line.strip().split(' ')[4]]
		playerArrays.append(playerArray)
	else : pointArray.append(line.strip())

def calculateGames(pointArray):
	print("hey")

print(pointArrays, gameArrays, playerArrays)


	


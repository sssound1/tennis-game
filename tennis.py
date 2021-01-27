file1 = open('full_tournament.txt', 'r');
Lines = file1.readlines()
Lines.append("\nM")

pointArrays = [] # [[0,1,1],[1,1,0,0],..]
gameArrays = [] # [[2, 1], [2, 1], ..]
playerArrays = [] # [[A,C], [A,B], ...]

# Score Match 01: Player playerArrays[0] gameArrays[0][0] > [0][1]? playerArrays[1]
# gameArrays[0][0] sets to [0][1]

# Games Player A
# wins = 0 , lose = 0
# for i,array in playerArrays:
# 	index= array.find(A), if index = 0, wins += pointArrays[i].count(0)  loses += len(pointArrays[i]) - pointArrays[i].count(0)
# pring win, lose 

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


	


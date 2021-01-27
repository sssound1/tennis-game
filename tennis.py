import sys
import re
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
	L = 0
	R = 0
	game = [0,0]
	for point in pointArray:
		point = int(point)
		if point == 0 : 
			L += 1
		if point == 1 : 
			R += 1
		if L >= 3 and R >= 3 :
		    if L - R > 1:
		    	game[0] += 1
		    	L = 0
		    	R = 0
		    elif R - L >1:
		    	game[1] += 1
		    	L = 0
		    	R = 0
		elif L == 4 and R <= 2 :
			game[0] += 1
			L = 0
			R = 0
		elif R == 4 and L <= 2 :
			game[1] += 1
			L = 0
			R = 0
	return game

pointArray = []

for line in Lines:
	if line.strip() == "":
		continue
	if line.strip()[0] == 'M':
		if len(pointArray) > 0 : 
			gameArray = calculateGames(pointArray)
			gameArrays.append(gameArray)
			pointArrays.append(pointArray)
		pointArray = []
	elif line.strip()[0] == 'P':
		playerArray = [line.strip().split(' ')[1],line.strip().split(' ')[4]]
		playerArrays.append(playerArray)
	else : pointArray.append(line.strip())

print(pointArrays, gameArrays, playerArrays)

complete_input = sys.stdin.read()
commands = complete_input.split("\n")
for command in commands:
	if command.strip() == "":
		continue
	if command.strip()[0] == "S":
		matchId = int(command.split(" ")[2]) - 1
		output = ""
		if gameArrays[matchId][0] > gameArrays[matchId][1] :
			output = " defeated Person "
		elif gameArrays[matchId][0] < gameArrays[matchId][1]: 
			output = " was defeated By Person "
		else :
			output = " was tied with "
		print("Person ", playerArrays[matchId][0], output , playerArrays[matchId][1])
		print(str(gameArrays[matchId][0]) + " sets to " + str(gameArrays[matchId][1]))
	if command.strip()[0] == "G":
		person = command.split(" ")[3]
		wins = 0
		loses = 0
		for i in range(len(playerArrays)):
			index = 0
			try :
				index = playerArrays[i].index(person)
			except :
				if i + 1 == len(playerArrays) : 
					print(str(wins) + " " + str(loses))
					exit(1) 
				else : continue
			if index == 0 : 
				wins += pointArrays[i].count("0")
				loses += len(pointArrays[i]) - pointArrays[i].count("0")
			else : 
				wins += len(pointArrays[i]) - pointArrays[i].count("0")
				loses += pointArrays[i].count("0")
		print(str(wins) + " " + str(loses))

# should be regex don't know why it doesn't work here take the simpler way
# matched = bool(re.match("/Score Match [0-9][0-9]/g", 
# complete_input.split("\n")[0]))





	


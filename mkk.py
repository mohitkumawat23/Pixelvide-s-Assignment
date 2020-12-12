from random import choice

players = []
file = open('TeamNa.txt', 'r')
players = file.read().splitlines()
print('Players:', players)

teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('Team names:', teamNames)


teamA = []
teamB = []
teamC = []
teamD = []
teamE = []
teamF = []
teamG = []
teamH = []

while len(players) > 0:
  

  playerA = choice(players)
  teamA.append(playerA)
 
  players.remove(playerA)
  

  if players == []: 
    break
  

  playerB = choice(players)
  teamB.append(playerB)

  players.remove(playerB)

  
  playerC = choice(players)
  teamC.append(playerC)
  
  players.remove(playerC)


  playerD = choice(players)
  teamD.append(playerD)
 
  players.remove(playerD)


  playerE = choice(players)
  teamE.append(playerE)
  
  players.remove(playerE)

  playerF = choice(players)
  teamF.append(playerF)
 
  players.remove(playerF)

  playerG = choice(players)
  teamG.append(playerG)
  
  players.remove(playerG)


  playerH = choice(players)
  teamH.append(playerH)
 
  players.remove(playerH)


teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)
teamNameC = choice(teamNames)
teamNames.remove(teamNameC)
teamNameD = choice(teamNames)
teamNames.remove(teamNameD)
teamNameE = choice(teamNames)
teamNames.remove(teamNameE)
teamNameF = choice(teamNames)
teamNames.remove(teamNameF)
teamNameG = choice(teamNames)
teamNames.remove(teamNameG)
teamNameH = choice(teamNames)
teamNames.remove(teamNameH)





print('\nHere are your GROUP:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)
print(teamNameC, teamC)
print(teamNameD, teamD)
print(teamNameE, teamE)
print(teamNameF, teamF)
print(teamNameG, teamG)
print(teamNameH, teamH)
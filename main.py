import random
import time
  
def laserbeam(bot):
  
  return bot-25
  
def superRepairKit(bot):
  
  return 100
  
def flamethrower(bot):
  
  return bot-10
  
def armSword(bot):
  
  return bot-10
  
def jeopardyBeam():
  
  a = random.randint(1,3)
  
  if a == 2:
    
    return 0
    
  else:
    
    return 1
  
def airSupport(bot):
  
  if bot+25 > 100:
    return 100
  else:
    return bot + 25

def pickChoice(robot, enemy):
  
  if enemy >= 90:
    
    return 6
    
  elif enemy > 50:
    
    return 1
  
  elif enemy < 40:
    
    return 3
    
  else:
    
    return 5
  
#tell what the game is about
print("Welcome to Build Your Robot! In this game you will build your own robot and fight another with your op robot!")
play = input("Press Enter to Start")
if play != "":
  play = input("Please Press Enter")
print("")

#show the abilities
numberList = ["1","2","3","4","5","6","7"]
damageTools = {"Laserbeam":laserbeam, "Flamethrower":flamethrower, "Arm Sword":armSword}
protectionTools = {"Air Support":airSupport, "Super Repair Kit":superRepairKit}
robot = []
robotAmmo = {"Laserbeam":2, "Super Repair Kit":1, "Air Support":5, "Flamethrower":300, "Arm Sword":300, "Jeopardy Beam":1}
enemy = ["Laserbeam", "Air Support", "Arm Sword", "Jeopardy Beam"]
enemyNum = [1,3,5,6]
enemyAmmo = {"Laserbeam":2, "Super Repair Kit":1, "Air Support":5, "Flamethrower":300, "Arm Sword":300, "Jeopardy Beam":1}
translateItem = {1:"Laserbeam", 2:"Super Repair Kit", 3:"Air Support", 4:"Flamethrower", 5:"Arm Sword", 6:"Jeopardy Beam", 7:"Shield"}
print("Here is the tools and the description of the tools that you can add to your robot:")
print("1. Lasergun: 25 Attack Damage | Can Only Use Twice")
print("2. Super Repair Kit: Heals to 100 Hearts | Can Only Once")
print("3. Air Support: Heals 20 Hearts | Can Use 5 Times") 
print("4. FLamethrower: 10 Attack Damage | Can Use Infinite Times")
print("5. Arm Sword: 10 Attack Damage | Can Use Infinte Times")
print("6. Jeopardy Beam: Takes 75 Hearts From Oppenent but Has A Chance of BackFire | Can Use Once")
print("7. Shield: Gain 30 Extra Hearts | Only Works at Beginnging")
print("")

for i in range(4):
  while True:
    addItem = input("What would you like to add to your robot?(Type in the Number of your Item) ")
    if addItem in numberList:
      break
    else:
      print("Invalid Input. Please add a valid input.")
    
  robot.append(translateItem[int(addItem)])
  print("You added the " + translateItem[int(addItem)] + "!")
  
print("")
playerBot = 100
if "Shield" in robot:
  playerBot = 130
otherBot = 100
print("Now it's time to fight the other robot!")
print("")
print("Your Bot HP: " + str(playerBot))
print("Other Bot HP: " + str(otherBot))

while otherBot > 0 and playerBot > 0:
  jList = [playerBot, otherBot]

  print("")
  
  while True:
    tool = input("What tool would you like to use?(Type in the Number of your Item)")
    while tool not in numberList:
      print("Invalid Input.")
      tool = input("What tool would you like to use?(Type in the Number of your Item)")
    tool = int(tool)
    if translateItem[tool] not in robot:
      print("You don't have that equipped.")
      
    elif robotAmmo[translateItem[tool]] != 0:
      break
    
    else:
      print("Your item can't be used.")
  if translateItem[tool] in damageTools:
    otherBot = damageTools[translateItem[tool]](otherBot)
    robotAmmo[translateItem[tool]] = robotAmmo[translateItem[tool]] - 1
  elif translateItem[tool] in protectionTools:
    playerBot = protectionTools[translateItem[tool]](playerBot)
    robotAmmo[translateItem[tool]] = robotAmmo[translateItem[tool]] - 1
  else:
    robotAmmo[translateItem[tool]] = robotAmmo[translateItem[tool]] - 1
    result = jeopardyBeam()
    jList[result] = jList[result] - 75
    playerBot = jList[0]
    otherBot = jList[1]
    
    
  print("You used your " + translateItem[tool] + "!")
  print("")
  print("Your Bot HP: " + str(playerBot))
  print("Other Bot HP: " + str(otherBot))

  if otherBot <= 0 or playerBot <= 0:
    break

  print("")
  tool = pickChoice(playerBot, otherBot)
  while True:
    
    if enemyAmmo[translateItem[tool]] != 0:
      break
    
    else:
      tool = enemyNum[random.randint(0,3)]
    
  print("The enemy used " + translateItem[tool] + "!")
  if translateItem[tool] in protectionTools:
    otherBot = protectionTools[translateItem[tool]](otherBot)
    enemyAmmo[translateItem[tool]] = enemyAmmo[translateItem[tool]] - 1
  elif translateItem[tool] in damageTools:
    playerBot = damageTools[translateItem[tool]](playerBot)
    enemyAmmo[translateItem[tool]] = enemyAmmo[translateItem[tool]] - 1
  else:
    enemyAmmo[translateItem[tool]] = enemyAmmo[translateItem[tool]] - 1
    #jList[0], jList[1] = jList[1], jList[0]
    result = jeopardyBeam()
    jList[result] = jList[result] - 75
    playerBot = jList[0]
    otherBot = jList[1]
    
  print("Your Bot HP: " + str(playerBot))
  print("Other Bot HP: " + str(otherBot))
  
if otherBot > playerBot:
  print("You lost :(")
  
else:
  print("You won! :)")

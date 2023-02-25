
#greet user
import random


print("Hi there.")
print()
rules = "Here are the rules: two players secretly pick one of \"rock,\" \"paper,\"or \"scissors.\" \
Both players reveal their selection to the other player at once; the winner is chosen \
based on what the selections are. Rock beats scissors (by crushing them); scissors\
beats paper (by cutting it); and paper beats rock (by covering it). If both players\
select the same one, it is a tie"

print(rules)
print()

play = False
name = input("Choose your weapon... rock, paper, or scissors: ")
while (name.lower() != "rock" and name.lower() != "paper" and name.lower() != "scissors"):
    name = input("Invalid choice. Choose your weapon: rock, paper, or scissors: ")

print("Your choice is", name,"!")
print("Computer choosing . . .")
l = ["rock","paper","scissors"]
comp = random.choice(l)
print("Those computer chose", comp, "!")
if (comp == "scissors"):
  if (name == "paper"):
    print("You lost!")
  elif (name == "rock"):
    print("You won!")
  else:
    print("You tied!")
    play = True
elif (comp == "rock"):
  if (name == "paper"):
    print("You won!")
  elif (name == "rock"):
    print("You tied!")
    play = True
  else:
    print("You lost!")
else: #paper
  if (name == "paper"):
    print("You tied!")
    play = True
  elif (name == "rock"):
    print("You lost!")
  else:
    print("You won!")

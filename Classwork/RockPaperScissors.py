import random
import sys

options = ["rock" , "scissors", "paper"] 

computerChoice = random.choice(options) 

yourChoice =  input("Pick rock , paper or scissors")

if yourChoice != "rock" or "scissors" or "paper":
   print("Sorry invalid term please try again.") 
   sys.exit()
 


if yourChoice == computerChoice:
  print(f"IT was a tie!! You chose {yourChoice} and the computer chose {computerChoice}!!")

elif yourChoice == "paper" and computerChoice == "rock":
  print(f"YOU won!! You chose {yourChoice} and the computer chose {computerChoice}!!")

elif yourChoice == "rock" and computerChoice == "scissors":
  print(f"YOU won!! You chose {yourChoice} and the computer chose {computerChoice}!!")

elif yourChoice == "scissors" and computerChoice == "paper":
  print(f"YOU won!! You chose {yourChoice} and the computer chose {computerChoice}!!")

else:
  print(f"Sorry but you lost. You chose {yourChoice} and the computer chose {computerChoice}!!")

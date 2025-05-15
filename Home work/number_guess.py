import random
number = random.randint(1,100)
print("This is a number guessing game")
print("Guess a number between 1 and 20:     ")

attempts = 0

while True:
    attempts=+1

    guess = int(input("TYpe a number betwwen 1 and 20"))

    if guess > number:
        print("That is to high")

    elif guess < number:
        print("That is to low")
    
    else:
        print("That is correct congradulations")
        break
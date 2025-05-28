import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        choice = input("Roll the dice? (yes/no): ").strip().lower()
        
        if choice == 'yes':
            result = roll_dice()
            print(f"You rolled a {result}!")
            
            if result == 6:
                print("Congratulations! You got the highest roll.")
            elif result == 1:
                print("Ouch! That's the lowest roll.")
            
        
            return result
        
        elif choice == 'no':
            print("Thanks for playing!")
            return None
        
        else:
            print("Please type 'yes' or 'no'.")


rolled_number = main()

if rolled_number is not None:
    print(f"Returned rolled number: {rolled_number}")

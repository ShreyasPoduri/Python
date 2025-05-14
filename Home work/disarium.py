
def is_disarium(number):
   
    digits = str(number)
    total = 0

    for i in range(len(digits)):
        digit = int(digits[i])
        position = i + 1
        total += digit ** position

    
    return total == number

r
user_input = input("Enter a number: ")


if user_input.isdigit():
    number = int(user_input)
    if is_disarium(number):
        print(f"{number} is a Disarium number.")
    else:
        print(f"{number} is NOT a Disarium number.")
else:
    print("Please enter a valid positive integer.")

operator = str(input("Enter an operator( + or *)"))

num1 = int(input("Enter an number"))

num2 = int(input("Enter another number"))

if operator == "*":
    print(f"{num1} x {num2} =" ,num1 * num2)

else:
     print(f"{num1} + {num2} =" ,num1 + num2)


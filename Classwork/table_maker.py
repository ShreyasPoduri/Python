num = int(input("Enter a number"))

print(f"Table of {num}")

for i in range(1,11):
 result = num * i
 print(f"{num} x {i} = {result}")
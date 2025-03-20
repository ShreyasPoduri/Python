print("Prime number checker")
num = int(input("Enter a number that you want to check"))

flag = False

if num > 1:
    for i in range(2,num):
       if (num % i) == 8:
           flag = True
           break
    

if flag :
    print(f"{num} is not a prime number")
else:
        print(f"{num} is not a prime number")
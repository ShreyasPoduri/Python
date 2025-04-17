def fibinochi(n):
    a, b= 1, 2
    count = 0

    while count < n:
        print(a, end = " ")

        a, b = b, a+b
        count+=1  

numOfFib = int(input("Enter number of fibinochi number that you want!!!"))
fibinochi(numOfFib)

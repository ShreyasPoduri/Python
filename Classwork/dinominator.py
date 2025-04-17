def no_notes(a):
    Q = [2000,500,200,100,50,20,10]   
    x = 0

    for i in range(7):
        q = Q[i]
        x = a//q
        print(f"Notes of {q} = {x}")

amount = int(input("Enter an amount"))
no_notes(amount)
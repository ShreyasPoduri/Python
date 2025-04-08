x = int(input("Enter the base (x): "))
n = int(input("Enter the number of terms (n): "))

series = ""

for i in range(n):
    term = x ** i
    series += str(term)
    
    if i != n - 1:
        series += " + "
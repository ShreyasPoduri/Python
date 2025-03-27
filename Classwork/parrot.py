class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
     return(f"{self.name} is {self.age} years old!!")


p1_name = str(input("Enter a name of your first parrot"))
p2_name = str(input("Enter a name of your second parrot"))

p1_age = int(input("Enter a age of your first parrot"))
p2_age = int(input("Enter a age of your second parrot"))


p1 = parrot(p1_name, p1_age )
p2 = parrot(p2_name, p2_age )

print(f"{p1.name} is a {p1.species}")
print(f"{p2.name} is a {p1.species}")

print(f"{p1.name} is {p1.age} years old!!")
print(f"{p2.name} is {p2.age} years old!!")

print(p1.intro())
print(p2.intro())

file = open("Codingal.txt","r")
counter = 0

content = file.read()
CoList = content.split("\n")

for i in CoList:
    if i :
        counter+=1

print(f"The number of lines in you file is {counter}")
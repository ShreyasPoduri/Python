file = open("Codingal.txt","r")
print(file.read())
file.close


file = open("Codingal.txt","r")
print("Read in parts\n")
print(file.read(12))
file.close

file = open("Codingal.txt","a")
file.write("Hi i am shreyas")
file.close
file = open("Codingal.txt","r")
print("File in read mode!\n")
print(file.read())
file.close


file = open("Codingal.txt","w")
print("File in write mode\n")
print(file.write("Hello my name is shreya san d I am 11 years old"))
file.close

file_append = open("Codingal.txt","a")
print("File in append mode\n")
print(file.write("Hello my name is shreya san d I am 11 years old"))
file.close
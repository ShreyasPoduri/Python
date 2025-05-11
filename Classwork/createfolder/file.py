newfile = open('Newfile.txt','x')
newfile.close

file = str(input("Type a file name.PLs add the .txt at the end"))
import os

print("If file exists or not, checker")
if os.path.exists(file):
    remove = bool(input("Type in true  or false with capital at the start"))
    if remove ==True:
       os.remove(file)
else:
    print("File does not exist")     


newfile = open("Newfile.txt" ,"w")
newfile.write("HI my name is shreyas and I am 12 years old")
newfile.close()

os.remove("Codingal.txt")

os.rmdir("new folder")
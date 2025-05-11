with open("Codingal.txt","w") as f:
   f.write("HEllo my name is shreyas!!! :)")
f.close()

with open("Codingal.txt","r") as f:
   data = f.readlines()
   print("Words in this file are ")
   for line in data:
      word = line.split
      print(word)
f.close()
   
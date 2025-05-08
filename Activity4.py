file1 = open("CodingalUpdated.txt","r")
file2 = open("CodingalUpdated.txt","w")

for line in file1.readlines():
   if not (line.startswith("Codingal")):
      print(line)
      file2.write(line)



file1.close()
file2.close()
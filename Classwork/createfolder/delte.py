inputfile = open("CodingalUpdated.txt","r")

outputfile = open("Codingal.txt","r")

lines_seen = set()
print("Eliminating xtra lines")

for line in inputfile:
    if line not in lines_seen:
        outputfile.write(line) 
        lines_seen.add(line)   

inputfile.close()
outputfile.close()
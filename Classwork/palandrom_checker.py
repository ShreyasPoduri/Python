word = str(input("Enter a word to check if it is a palandrom"))
def palandrom(word):
  left_pos = 0
  right_pos = len(word) - 1

  while right_pos >= left_pos:
   if not word[left_pos] == word[right_pos]:
    return False
   
   right_pos-= 1 
   left_pos +=1
   return True
if (palandrom(word)):
 print(f"{word} is a palandrom")
else:
 print(f"{word} is not a palandrom")
  


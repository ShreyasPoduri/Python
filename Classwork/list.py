list = ["apple" ,'banana' ,'guava' ,'kiwi' ,'mango']
print("Lenght of list",len (list))

print("First element =",list[0])

print("Last element =",list[-1])

list.append("orange")
print("Updated list =",list)

list.remove("apple")
print("Updated list =",list)

list.sort()
print("Sorted list =",list)

list.pop(1)
print("Updated list =",list)

list.reverse()
print("Reversed list =",list)

print("Multiplication on list =",list*2)

list = list[:4]
print("sliced list =",list)

list.clear()
print("Updated list =",list)
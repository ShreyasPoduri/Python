my_dict = {'name':'jack','age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 11
print(my_dict)

my_dict['Adress'] = 'Downtown'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Adress:", my_dict.get("Adress"))

my_dict.clear()
print(my_dict)
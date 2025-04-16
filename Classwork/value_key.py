
my_dict = {
    "name": "Shreyas",
    "age": 12,
    "city": "Stockgholm",
    "language": "Telugu",
    "hobby": "Football"
}

user_key = input("Enter a key (e.g., name, age, city, language, hobby): ")

if user_key in my_dict:
    print(f"The value for key '{user_key}' is: {my_dict[user_key]}")
else:
    print(f"Key '{user_key}' not found in the dictionary.")

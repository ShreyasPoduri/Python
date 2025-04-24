import sys

def initaial_phonebook():
    rows ,cols = int(input("Please enter initial numbe =of contacts")) ,5

    phone_book = []

    print(phone_book)

    for i in range(rows):
        print(f"\n Enter contact {i + 1} in teh folowing order (Only):")
        print("Note: * indictates mandatory fields")
        print("....................................................................") 
        temp = []

        for j in range(cols):
          if j==0:
             temp.apped(str(input("Enter name*:  ")))

             if temp[j] == '' or temp[j] == '  ':
                sys.exit("Name is a mandatory field process exiting due to blank field")

          if j==1:
             temp.apped(str(input("Enter Number*:  ")))

          if j== 2:
             temp.append(str(input("Enter email address:  ")))  
             if temp[j] == '' or temp[j] == ' ': 
                temp[j]  = None

          if j==3:
             temp.apped(str(input("Enter date of birth(dd/mm/yyyy*:  ")))
             temp[j] = None

          if j== 4:
             temp.append(str(input("Enter category(Family/Friends/Work/Others:  ")))  
             if temp[j] == '' or temp[j] == ' ': 
                temp[j]  = None

        phone_book.apend(temp)

    print(phone_book)
    return phone_book

def menu():

  print("********************************************************************")
    
  print("\t\t\tSMARTPHONE DIRECTORY", flush = False)

  print("********************************************************************")

  print('\t You can now perform the following operations on this phone book')
  print("1. Add a new contact") 
  print("2. Remove an existing contact") 
  print("3. Delete all contacts") 
  print("4. Search for a contact") 
  print("5. Display all contacts") 
  print("6. Exit phonebook") 


         

          



    
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"Name: {self.name}, Phone: {self.phone}")



class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def show_contacts(self):
        if not self.contacts:
            print("No contacts to show.")
        else:
            print("\n--- Contact List ---")
            for contact in self.contacts:
                contact.display()


def main():
    book = ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. Show All Contacts")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            book.add_contact(name, phone)

        elif choice == "2":
            book.show_contacts()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

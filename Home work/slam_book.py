# Basic SLAM book program

def collect_friend_info():
    print("\n--- Welcome to My SLAM Book ---\n")
    name = input("Your Name: ")
    nickname = input("Your Nickname: ")
    birthday = input("Your Birthday (DD/MM/YYYY): ")
    hobbies = input("Your Hobbies: ")
    favorite_color = input("Your Favorite Color: ")
    crush = input("Your Crush (Just for fun!): ")
    message = input("Your Message for Me: ")

    # Store the info in a dictionary
    friend_info = {
        "Name": name,
        "Nickname": nickname,
        "Birthday": birthday,
        "Hobbies": hobbies,
        "Favorite Color": favorite_color,
        "Message": message
    }

    return friend_info


# Save multiple entries
def main():
    slam_book = []

    while True:
        info = collect_friend_info()
        slam_book.append(info)
        print("\nThanks for filling the SLAM book!")

        another = input("\nDo you want to add another friend? (yes/no): ").lower()
        if another != "yes":
            break

    # Display all entries
    print("\n--- SLAM Book Entries ---")
    for i, entry in enumerate(slam_book, 1):
        print(f"\nFriend #{i}")
        for key, value in entry.items():
            print(f"{key}: {value}")

# Run the program
if __name__ == "__main__":
    main()

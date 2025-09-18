users = []

# Create
def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    new_id = users[-1]["id"] + 1 if users else 1
    users.append({"id": new_id, "name": name, "email": email})
    print(f"User '{name}' added.\n")

# Read
def read_users():
    if not users:
        print("No users found.\n")
    else:
        for user in users:
            print(user)
        print()

# Update
def update_user():
    user_id = int(input("Enter user ID to update: "))
    for user in users:
        if user["id"] == user_id:
            name = input("Enter new name (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print(f"User {user_id} updated.\n")
            return
    print("User not found.\n")

# Delete
def delete_user():
    user_id = int(input("Enter user ID to delete: "))
    global users
    users = [user for user in users if user["id"] != user_id]
    print(f"User {user_id} deleted (if existed).\n")

# Menu
def menu():
    while True:
        print("Choose an option:")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            create_user()
        elif choice == "2":
            read_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.\n")

menu()

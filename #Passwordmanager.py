#Passwordmanager
import random
import string
#import _tkinter as tk
Pincode = 'example1234'

def Login():
    pass
    global Pincode
    while True:
        Pincode = input("Enter your pincode: ")
        if Pincode == 'example1234':
            print("Login successful")
            break
        else:
            print("Incorrect pincode. Please try again.")

Login()
print("Welcome to Passwordmanager.")

passwords = {}
def generate_password():
    s = string.ascii_letters + string.digits
    symbol = string.punctuation
    s += symbol
    for i in range(16):
        password = "".join(random.sample(s, 16))
    return password    


def add_password():
    password = None  # Инициализация переменной password
    
    account = input('Enter the name of the service/app: ')
    print("Do you want to generate a password for", account, " or add manually? (g/m)")
    
    choice = input().lower()
    while choice != "g" and choice != "m":
        print("Invalid choice, press 'g' or 'm'")
        choice = input().lower()
    
    if choice == "g":
        while True:
            password = generate_password()
            print("Password for", account, "is:", password, "Do you want to save it? (y/n)")
            choice = input().lower()
            while choice != "y" and choice != "n":
                print("Invalid choice, press 'y' or 'n'")
                choice = input().lower()
            if choice == "y":
                passwords[account] = password
                print("Pasword: ",password,"for: ",account,"is added successfully")
                break
            elif choice == "n":
                print("Generating another password...")
    elif choice == "m":
        while True:
            passwordinput = input("Enter the password manually: ")
            print("Password for", account, "is:", passwordinput, "Do you want to save it? (y/n)")
            choice = input().lower()
            while choice != "y" and choice != "n":
                print("Invalid choice, press 'y' or 'n'")
                choice = input().lower()
            if choice == "y":
                passwords[account] = passwordinput
                print("Pasword: ",passwordinput,"for: ",account,"is added successfully")
                break
            elif choice == "n":
                print("Please re-enter the password")
           

def menu():
    pass
    while True:
        print("1. Add a new password")
        print("2. View passwords")
        print("3. Update a password")
        print("4. Delete a password")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            for account, password in passwords.items():
                print(account, ":", password)
        elif choice == "3":
            if not passwords:
                print("No passwords to update")
            else:
                account = input("Enter the name of the account/service to update: ")
                if account not in passwords:
                    print("Account/Service not found,please enter a valid account")   
                elif account in passwords:
                    print("Do you want to generate a new password or add manually? (g/m)")
                    choice = input().lower()
                    while choice != "g" and choice != "m":
                        print("Invalid choice, press 'g' or 'm'")
                        choice = input().lower()
                    if choice == "g":
                        new_password = generate_password()
                        passwords[account] = new_password
                        print("Password updated successfully")
                    elif choice == "m":
                        new_password = input("Enter the new password: ")
                        passwords[account] = new_password
                        print("Password updated successfully")
                    else:
                        print("Account/Service not found")
        elif choice == "4":
            if not passwords:
                print("No passwords to delete")
            else:
                account = input("Enter the name of the account/service to delete: ")
                if account in passwords:
                    del passwords[account]
                    print("Password deleted successfully")
                else:
                    print("Account/Service not found")
        elif choice == "5":
            print("Exiting the password manager")
            break

        else:
            print("Invalid choice")

menu()


                

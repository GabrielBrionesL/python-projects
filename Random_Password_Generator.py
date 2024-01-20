import string
import random

# This is a list of characters from which we want to generate our password
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# Create function to generate random password
def generate_password():
    # If yes, ask for password length
    password_length = int(input("How long would you like your password to be? ")) 

    # Shuffle the list of characters into random order
    random.shuffle(characters)

    password = []

    # Add random character to empty list based on the length of password
    for c in range(password_length):
        password.append(random.choice(characters))
    
    # To make it more unique, we shuffle it again to make it more random
    random.shuffle(password)

    # Initialize as a string from a list
    password = "".join(password)

    # Print the password
    print(password)

# Ask user to generate password with Yes or No as the answer
ask_password = input("Do you want to generate a password? (Yes/No): ")

if ask_password == "Yes":  # For security reasons, we will not convert to lower to allow more flexibility in user input
    generate_password()
elif ask_password == "No":  # If initial response is no, exit program
    print("Program ended")
    quit()
else:
    print("Invalid input. Please input Yes or No")
    quit()
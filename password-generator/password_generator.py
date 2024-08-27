import random

# Lists of possible characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# User inputs for the number of letters, symbols, and numbers
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level - Password in order of letters, symbols, numbers
easy_password = ""

# Add the specified number of random letters to the password
for _ in range(nr_letters):
    easy_password += random.choice(letters)

# Add the specified number of random symbols to the password
for _ in range(nr_symbols):
    easy_password += random.choice(symbols)

# Add the specified number of random numbers to the password
for _ in range(nr_numbers):
    easy_password += random.choice(numbers)

print(f"Easy Level Password: {easy_password}")

# Hard Level - Password with characters in random order
# First, create a list of all selected characters
password_list = []

# Add the specified number of random letters to the list
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add the specified number of random symbols to the list
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add the specified number of random numbers to the list
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Randomize the order of the characters in the list
random.shuffle(password_list)

# Convert the list to a string
hard_password = ''.join(password_list)

print(f"Hard Level Password: {hard_password}")

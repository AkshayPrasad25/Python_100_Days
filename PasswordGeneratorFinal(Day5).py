#random.shuffle(x) function used to shuffle the list items
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PythonPassword Generator!")
no_letters= int(input("How many letters would you like in your password?\n")) 
no_symbols = int(input(f"How many symbols would you like in your password?\n"))
no_numbers = int(input(f"How many numbers would you like in your password?\n"))
password_list=[]
for char in range(1,no_letters+1):
    password_list.append(random.choice(letters))
for num in range(1,no_numbers+1):
    password_list.append(random.choice(numbers))
for sym in range(1,no_symbols+1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
generated_password=""
for item in password_list:
    generated_password+=item

print(f"Generated password is: {generated_password}")

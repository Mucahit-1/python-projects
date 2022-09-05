#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
level_of_password = int(input("for easy password press 0 , for hard press 1\n"))

if level_of_password == 0:

  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  password1 = ""
  for char in range(1 , nr_numbers + 1):
    password1 += random.choice(numbers)

  password2 = ""
  for char in range(1 , nr_letters + 1):
    password2 += random.choice(letters)

  password3 = ""
  for char in range(1 , nr_symbols + 1):
    password3 += random.choice(symbols)

  password = password1 + password2 + password3
  print(password)

elif level_of_password == 1:

  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  password_list = []

  for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

  for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

  print(password_list)
  random.shuffle(password_list)
  print(password_list)

  password = ""
  for char in password_list:
    password += char

  print(f"Your password is: {password}")
  
else:
  print("please press 0 or 1")  
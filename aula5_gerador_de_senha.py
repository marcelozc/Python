import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = letters[random.randint(0,51)]

for caracter in range (1,nr_letters):
  password = password + letters[random.randint(0,51)]

for caracter in range (1,nr_symbols+1):
  password = password + symbols[random.randint(0,8)]

for caracter in range (1,nr_numbers+1):
  password = password + numbers[random.randint(0,8)]

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list_password = []

for char in password:
  list_password += char

print(list_password)

random.shuffle(list_password)

print(list_password)

password_random = ""

for x in list_password:
  password_random += x

print(password_random)

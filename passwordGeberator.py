#
# import string
#
# # define the alphabet
# letters = string.ascii_letters
# print(letters)
#
# digits = string.digits
# print(digits)
#
# special_chars = string.punctuation
# print(special_chars)

# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)
# print(string.whitespace)


# import string

# print("Choose the Option from here: \n1. Digit\n2. Letter\n3. Special Cheracture\n4. Exit ")
# characterList = ""
# while(True):
#     choice = int(input("Enter the Option: "))
#
#     if choice == 1:
#         characterList += string.digits
#         print(characterList)
#         break
#     elif choice == 2:
#         characterList += string.ascii_letters
#         print(characterList)
#         break
#     elif choice == 3:
#         characterList += string.punctuation
#         print(characterList)
#         break
#     elif choice == 4:
#         break
#     else:
#         print("Please Pick Right Option... ")



# import string
# import random
#
# lettes = string.ascii_letters
# digits = string.digits
# symbol = string.punctuation
#
# nr_letter = int(input("How Many Latters? "))
# nr_digit = int(input("How Many Digits? "))
# nr_symbol = int(input("How Many Symbol? "))

#   Easy Level
# password = ""
# for char in range(1, nr_letter + 1):
#     password += random.choice(lettes)
# for char in range(1, nr_digit + 1):
#     password += random.choice(digits)
# for char in range(1, nr_symbol + 1):
#     password += random.choice(symbol)
# print(f"Your String Password is: {password}")
#
#
# #   Hard level
# password_list = []
# for char in range(1, nr_letter + 1):
#     password_list.append(random.choice(lettes))
# for char in range(1, nr_digit + 1):
#     password_list.append(random.choice(digits))
# for char in range(1, nr_symbol + 1):
#     password_list.append(random.choice(symbol))
# password = ""
# for char in password_list:
#     password += char
# print(password)




# import string
# import random
#
# lettes = string.ascii_letters
# digits = string.digits
# symbol = string.punctuation
#
# nr_letter = int(input("How Many Latters? "))
# nr_digit = int(input("How Many Digits? "))
# nr_symbol = int(input("How Many Symbol? "))
#
# password = ""
# for char in range(1, nr_letter + 1):
#     password += random.choice(lettes)
# for char in range(1, nr_digit + 1):
#     password += random.choice(digits)
# for char in random.choice(symbol):
#     password += random.choice(symbol)
#
# print(password)


#   Hard Level

import string
import random

lettes = string.ascii_letters
digits = string.digits
symbol = string.punctuation
print("Welcome pyPassword")
nr_letter = int(input("How Many Letters? "))
nr_digit = int(input("How Many Digits? "))
nr_symbol = int(input("How Many Symbol? "))

password_list = []
for char in range(1, nr_letter + 1):
    password_list.append(random.choice(lettes))
for char in range(1, nr_digit + 1):
    password_list.append(random.choice(digits))
for char in range(1, nr_symbol):
    password_list.append(random.choice(symbol))

password = ""
for char in password_list:
    password += char
print(password)






































































































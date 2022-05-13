"""
Make strong password generator by python

*****Rules*****
1-Only Numbers
2-At least 6 number for the password
3-60% For letters (upper and lower)
4-40% for punctuation and digits

*****Logic*****
1-import string module and random
2-store all elements of password in lists
3-# Create a variable for password
4-Make sure that user's input is right
5-Make the password random by shuffle
6-Male sure that letters 60% and punctuation and digits 40%
7-creation of  strong password
8-shuffle again
9-Heeeey getting the strong password

"""


# import string module and random
import string
import random

# store all chars in lists
x1 = list(string.ascii_uppercase)
x2 = list(string.ascii_lowercase)
x3 = list(string.digits)
x4 = list(string.punctuation)

# Create a variable
chars_num =input("Please enter the number of password. ")

# Make sure that user's input is right
while True:
    try:
        chars_num = int(chars_num)
        if chars_num < 6:
            print("It's only allowed 6 characters ")
            chars_num = input("Please enter at least 6 characters. ")
        else:
            break

    except:
        print("Please enter only numbers. ")
        chars_num = input("Please enter the number of password. ")

# Make the password random
random.shuffle(x1)
random.shuffle(x2)
random.shuffle(x3)
random.shuffle(x4)

# --> to make letters 60%
part1 = round(chars_num*(30/100))
# --> to male digits and punctuation 40%
part2 = round(chars_num*(20/100))


password = []

# Create strong password
for i in range(part1):
    password.append(x1[i])
    password.append(x2[i])

for i in range(part2):
    password.append(x3[i])
    password.append(x4[i])

# random again
random.shuffle(password)

password = "".join(password[0:])

print("This is the password\n"+password)
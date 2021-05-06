#Create a Python program that generates a random password for
#the user. Make sure your program takes a few inputs from the user:
#How long should the password be?
#How many characters should there be?
#Should it have both uppercase and lowercase letters?
#Should it include numbers and special symbols, too?

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(_)}{]["

length = int(input("Enter password lenth "))
password=""
for i in range(length+1):
    password += random.choice(chars)
print(password)

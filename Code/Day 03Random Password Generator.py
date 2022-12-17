#--------------------------------------------------------| 100 Porjects in 100 Days|--------------------------------------------------------#
#day 03
# Project 03: Random Password Generator

# 1. Importing modules
import random

#welcoming user
print("Hello User : welcome to random password generator")
print("choosing a strong password is very important for your account security")
print("make sure your password is at least 8 characters long, contains both uppercase and lowercase letters, numbers and symbols")

while True:
    try:
        #taking input from user
        passlen = int(input("Enter the length of password: "))
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        p = "".join(random.sample(s,passlen ))
        print(p)
        break
    except ValueError:
        print("Please enter a valid number")
    
want_Save = input("Do you want to save your password? (y/n): ")

while True:
    if want_Save == "y":
        username = input("Enter your username: ")
        website = input("Enter the website name: ")
        output = (f"Username: {username} | Website: {website} | Password: {p}")
        with open("password.txt", "a") as f:
            f.write(output)
            print("Your password is saved in password.txt file")
            break
    elif want_Save == "n":
        print("Thank you for using our service")
        break
    else:
        print("Please enter a valid input")
        want_Save = input("Do you want to save your password? (y/n): ")
        username = input("Enter your username: ")

print("Thank you for using our service")


     








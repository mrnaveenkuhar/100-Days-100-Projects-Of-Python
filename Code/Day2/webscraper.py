# importing the modules
import requests
from bs4 import BeautifulSoup

# Getting the website
print("warning: This code is for educational purposes only. I am not responsible for any misuse of this code \n some websites don't allow webscraping so please use this code on your own risk")
website = input("Enter the website: \n-->")
for i in website:
    if ".com" not in website:
        print("Invalid input")
        website = input("Enter the website: \n-->")
    else:
        print("Getting the website: " + website)

# handling the exception
try:
    r = requests.get(website) # Getting the website
except Exception: # Handling the exception
    print("There was an error: either the website is not valid or the website is not available ")


# Getting the html content
htmlcontent = r.content # Getting the html content
print("Getting the html content")

# Parsing the html content
print("Parsing the html content")
soup = BeautifulSoup(htmlcontent, 'html.parser') # Parsing the html content

#Asking the user what to do
userinput  = input(''' what do you want to do?
S- Save the all html content
P- Print the all html content
F-Find the html content
E-exit
''')

# Converting the user input to uppercase
userinput = userinput.upper()

# Checking the user input
for i in userinput:
    if i == "P":
        print(soup.prettify()) # Printing the html content
    elif i == "S":
        filename = input("Enter the filename: \n-->")
        with open(filename, 'w') as f:
            f.write(soup.prettify()) # Saving the html content
    elif i == "F":
        Find = input("Enter the text to find: \n-->")
        if Find == None:
            print("No such element found")
        elif Find != None:
            print("Element found")
            print("what do you want to do with the element?")
            instruction=  input("P- Print the element\nS- Save the element\nE- Exit\n-->")
            instruction = instruction.upper()
            #handling the input
            for i in instruction:
                if i == "P":
                 print(soup.find(Find))
                elif i == "S":
                    filename = input("Enter the filename: \n-->")
                    try:
                        with open(filename,'w') as f:
                            f.write(f"{soup.find(Find)}")
                    except Exception:
                        print(f'''There was an error
                        either the file named {filename} is already present or the file is not valid 
                        what do you can do
                        1- Try again with a different file name
                        2- Delete the file named {filename} and try again
                        3 - report the bug to the developer''')

    elif i == "E":
        break
    else:
        print("Invalid input")

print("Thank You For Using The Program")
print("Made By: Naveen Kuhar @mrnaveenkuhar")
print("Github: www.github.com/mrnaveenkuhar")

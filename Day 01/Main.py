#importing the modules
from PIL import Image
import os
import shutil
#Moduels imported


take = input("Enter the path of your image: ")
raw = Image.open(take)
raw = raw.resize((128,128))
#Creating the output folder
if not os.path.exists("output"):
    os.mkdir("output")
else:
    pass
# move this file to output folder
raw.save("icon(128*128px).ico")
shutil.move("icon(128*128px).ico", "output")
# handling if file already exists
if os.path.exists("icon(128*128px).ico"):
    print("File already exists")
    input("Overwrite the file? (y/n): ")
    if input == "y":
        raw.save("icon(128*128px).ico")
        shutil.move("icon(128*128px).ico", "output")
        os.remove("icon(128*128px).ico")
    else:
        pass
else:
    pass
print("Your icon is ready")
print("Thank you for using this programme")


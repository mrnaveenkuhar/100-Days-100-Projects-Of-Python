import fileinput
import glob

# Find all the .txt files in the current directory
files = glob.glob("*.txt")

# Iterate through the files
for file in files:
  # Open the file for reading and writing
  with fileinput.input(file, inplace=True) as f:
    # Iterate through the lines in the file
    for line in f:
      # Replace the text and print the modified line
      print(line.replace("old text", "new text"), end='')

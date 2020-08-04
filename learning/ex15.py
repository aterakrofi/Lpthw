#Import the argemnets library
from sys import argv
#Definining parameters for the argument function
script, filename = argv
#Open the file and assign the command to variable txt
txt = open(filename)
#print the text to screen
print(f"Here's your file {filename}:")
#read the contents of the file
print(txt.read())
#Prompt user to type in filename and assign to file_name
print("Type the filename again:")
file_again = input("> ")
#assign opened file to txt_again
txt_again = open(file_again)
#read contents of file
print(txt_again.read())

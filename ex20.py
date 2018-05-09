#import the arguments library
from sys import argv
#define our arguments
script, input_file = argv
#function to read a line of text
def print_all(f):
    print(f.read())
#function to return the reader to the first line
def rewind(f):
    f.seek(0)
#function to print text line by line
def print_a_line(line_count, f):
    print(line_count, f.readline())
#assign the command openning of a file to current_file
current_file = open(input_file)

print("First let's print the whole file:\n")
#Parse a the variable to the function
print_all(current_file)

print("Now let's rewind, kind of like a a tape.")
#Parsing a variable to the function
rewind(current_file)

print("Let's print three lines:")
#assign a number to a variable
current_line = 1
#function prints line number 1
print_a_line(current_line, current_file)
#Function prints line no. 2 (variable + itself)
current_line = current_line + 1
print_a_line(current_line , current_file)
#function prints the 3rd line
current_line = current_line + 1
print_a_line(current_line, current_file)

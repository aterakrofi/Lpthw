#Import the argument parser library
from sys import argv
#Parse the variables script and filename to argv
script, filename = argv
#print the f-string with the variable filename
print(f"We're going to erase {filename}.")
#print text to screen
print("If you don't want that, hit CTR-C (^C).")
print("If you do want that, hit RETURN.")
#Prompt user
input("?")
#print text to screen
print("Opening file...")
#open txt file and assign command to target variable
target = open(filename,'w')
#print text to screen
print("Truncating the file. Goodbye!")
#empty the text file
target.truncate()
#print txt to screen
print("Now I'm going to ask you for three lines.")
#take prompt from user and assign to variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
#print text to screen
print("I'm going to write these to the file.")
#write text stored in the variables to the text file
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
#close the file
target.close()

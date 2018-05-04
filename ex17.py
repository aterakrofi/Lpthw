#import the libaries
from sys import argv
from os.path import exists
#define the argument parameters
script , from_file, to_file = argv
#print text to screen
print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
#read opened file
indata = in_file.read()
#print length of characters in the text file
print(f"The input file is {len(indata)} bytes long")
#determin if the file exists
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTR-C to abort.")
input()
#open destination file for writing
out_file = open(to_file, 'w')
#write destination file with data stored in variable indata
out_file.write(indata)
#print text to screen
print("Alright , all done.")
#close both file
out_file.close()
in_file.close()

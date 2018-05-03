from sys import argv

script, filename = argv

#open file
print("Opening file...")
read_text = open(filename)

print(read_text.read())

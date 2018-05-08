from sys import argv

script, filename = argv

#open file
print("Opening file...")
read_text = open(filename)

x = read_text.read()

print(x)

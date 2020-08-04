from sys import argv

script, filename = argv

def spit(filename):
    open_file= open(filename,'r')
    read_file = print(open_file.read())
    return read_file


spit(filename)

from sys import argv

#take four arguments variables and pack into argv
script ,header, body, footer = argv
#print first argument in an f-string
print(f"\n*******TEST RUN of {script}*******")
#print second argument
print(f"\n----------{header}------------")
#assign input to the variable first
first = input("\nFirst name: ")
#assign input to the variable last
last = input("Last name: ")
#assign input to the variable age
age = input("Age: ")
#print argument variable
print(f"\n--------{body}-----------------")
#print string and add space
print("\n",first, end =" ")
#print variable last and add space
print(last, end = " ")
#print variable age and add space
print(age , end= " ")
print(f"\n\n---------{footer}--------------")

#Assigning values(numbers and strings) to variables
types_of_people = 10
#formatting a variable within a string
x = f"There are {types_of_people} types of people."
# variable binary assigned the string binary
binary = "binary"
# variable do_not assigned the string do_not
do_not = "don't"
y = f"Those who {binary} and those who {do_not}."

#print results to screen
print(x)

print(y)
#print variable x in a string
print(f"I said: {x}")
print(f"I also said: '{y}'")
#print a variable containing a string together with another variable
hilarious = False
# Empty {} to hold the value of another variable
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)

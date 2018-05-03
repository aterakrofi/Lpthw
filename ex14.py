#import the arguments library
from sys import argv
# parsing the variables to the argv function
script, user_name , age, DOB = argv
#Assigning string to prompt variable
prompt = f" {user_name}>>> "
#printing username and script name in f-string
print(f"Hi {user_name}, I'm the {script} script.")
#printing string
print("I'd like to ask you a few questions.")
#print variable username in string using f-string
print(f"Do you like me {user_name}?")
#Store user input in varibale like. Prompt would display string
likes = input(prompt)
#print string with variable using f-string
print(f"Where do you live {user_name}?")
#Store keyboard input to lives
lives = input(prompt)
#Ask user a question
print("What kind of computer do you have?")
#store users response in variable computer
computer = input(prompt)
#printing mulitple lines of string and variables
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
{user_name}, {age} , {DOB}
""")

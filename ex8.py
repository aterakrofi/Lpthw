#Defining arguments for the variable formatter
formatter = "{} {} {} {}"
#pass the formatter 4 arguments 1,2,3,4
print(formatter.format(1, 2, 3, 5))
#pass the formatter 4 arguments : one, two, three and four
print(formatter.format("one", "two", "three", "four"))
#pass the formatter 4 boolean arguments , True, False, False, True
print(formatter.format(True, False, False, True))
#Pass the formatter itself as the argument
print(formatter.format(formatter, formatter, formatter, formatter))

#pass the strings as arguments
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

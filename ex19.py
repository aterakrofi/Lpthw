#defining the function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #block of code for the function
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
#parse two arguments 20 & 30 for the function
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
#defining two variables
amount_of_cheese = 10
amount_of_crackers = 50

#parsing two variables as arguments for the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
#Perform math operations and parse as arguments
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
#Combine variables with numbers and parse them as arguments for the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

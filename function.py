#function to calculate my rent
from sys import argv

script , a1, a2, a3, a4, a5 = argv

def calc (Tel , rent , cc , wage , tax) :
    expense = Tel + rent + cc
    income = wage + tax
    saving = income-expense
    print(f"You made ${income} this month")
    print(f"Your expenses total ${expense}")
    print(f"You you only have ${saving} in you account\n")

print("\nMethod 1 : Giving it raw values")
calc(30.00, 660.00, 150.00 , 1041 , 300.00)

print("Method 2: Parsing variabes : ")
metro = 30.00
JS = 660.00
bank = 150.00
oneder = 1041
IRS = 300.00
calc(metro, JS , bank , oneder , IRS)

print("Method 3 : Maths operations")
calc(30.00+105, 660*2 , 150/2, 1400+20, 30*10)

print("Method 4 : Parse argv")
calc(int(a1), int(a2), int(a3), int(a4), int(a5))

print("Method 5 : combine variables and numbers")
calc(metro-5, JS*2, bank -.05 , oneder/0.01 , IRS-100)

print("Method 6 : user input" )
input1 = input("tel  : ")
input2 = input("rent : ")
input3 = input("cc :")
input4 = input("wage :")
input5 = input("tax :")
calc(int(input1), int(input2), int(input3), int(input4), int(input5))

print("Method 7 read from file")
read_text = open('test2.txt')
x = read_text.readline()
y = read_text.readline()
z = read_text.readline()
a = read_text.readline()
b = read_text.readline()

calc(int(x), int(y), int(z), int(a), int(b))
read_text.close()

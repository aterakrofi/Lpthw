def calc (Tel , rent , cc , wage , tax) :
    expense = Tel + rent + cc
    income = wage + tax
    saving = income-expense
    print(f"You made ${income} this month")
    print(f"Your expenses total ${expense}")
    print(f" You you only have ${saving} in you account\n")

print("Method 7 read from file")

read_text = open('test2.txt')
#adobe =
x = read_text.readline()
y = read_text.readline()
z = read_text.readline()
a = read_text.readline()
b = read_text.readline()



print(x,y,z,a,b)

calc(int(x), int(y), int(z), int(a), int(b))

read_text.close()

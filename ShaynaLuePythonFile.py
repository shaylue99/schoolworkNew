#Shayna Lue - Average Function 

x = input('Please enter a number(or stop/end/quit to end): ')
numberlist = []
#sum = 1
#total = 0
while x not in ['stop', 'end', 'quit']:
    numberlist.append(int(x))
    mean = sum(numberlist)  / len(numberlist)
    print("Values: ", numberlist)
    print("Average = ", mean)
    x = input('Please enter a number(or stop/end/quit to end): ')


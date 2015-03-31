# Lab 7 problem 2
# Maximilian Lemos

def total_worth():
    filein = open('parts.txt','r')
    mystring = ""
    for i in filein:
        mystring = mystring + i.strip() + " "
    mystring = mystring.strip()
    helper_list = mystring.split(" ")
    daquant = helper_list[1::3]
    daprice = helper_list[2::3]
    length = len(daquant)
    counter = 0
    total = 0
    for i in range(length):
        item_value = eval(daquant[counter]) * eval(daprice[counter])
        counter = counter + 1
        total = item_value + total
    print("Total value of inventory: ")
    return total

 

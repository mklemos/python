# Lab5 problem 1
# Maximilian Lemos

a = []
while 0 not in a:
    user_input = input("put stuff in the list here, 0 kills the program: ")
    int_holder = int(user_input)
    while int_holder not in a:
        a.append(int_holder)
print("Here is the sum of unique items in the set: ")
print(sum(a))
print("Here is the unique set: ",a)



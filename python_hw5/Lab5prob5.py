# Lab5 problem 5
# Maximilian Lemos

# Two fxns:

def find_median(a):
    first = [int(i) for i in sorted(a)]
    x = first[4]
    y = first[5]
    answer = (x+y)/2
    return answer

def input_list():
    a = []
    for i in range(10):
        user_input = eval(input("put stuff in the list here: "))
        a.append(user_input)
    
    print("Median of list: ",find_median(sorted(a)))
input_list()

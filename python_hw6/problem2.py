# Lab 6 problem 2
# Maximilian Lemos

def first_five_powers(a):
    yield a
    yield a**2
    yield a**3
    yield a**4
    yield a**5

a = first_five_powers(7)

def print_um_out():
    num = eval(input("Please select a number: "))
    a = first_five_powers(num)
    for i in range(5):
        print(next(a), end=' ')

    #print(next(a),next(a),next(a),next(a),next(a), end=' ')

print_um_out()





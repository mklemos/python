# Lab5 problem 4
# Maximilian Lemos

# Takes GCD of two numbers using recursion.


def gcd_recur(a, b):
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)

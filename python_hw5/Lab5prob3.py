# Lab5 problem 3
# Maximilian Lemos

# Two fxns: First calculates LCM of two numbers.
# Second Takes GCD of two numbers.

def lcm_math(a,b):
    multiple = b
    for x in range(1000000):
        x = x + 1
        multiple = b * x
        if (multiple % a == 0):
            lcm = multiple
            break
    return multiple

def gcd_math(a,b):
    while b:
        a, b = b, a%b
    return a

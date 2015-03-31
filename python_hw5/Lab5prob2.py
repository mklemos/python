# Lab5 problem 2
# Maximilian Lemos

# Two fxns: One/Two that takes an integer/float representation of
# coins and gives the least amount of coins in change.

def change_machine_int(cost):
    coin_list = [25,10,5,1]
    remaining = 100 - cost
    change_returned = []
    for coin in coin_list:
        num_coins,remaining = divmod(remaining,coin)
        change_returned.append(int(num_coins))
    print(" Q"," D ","N ","P")
    return change_returned


def change_machine_float(cost):
    coin_list = [.25,.10,.05,.01]
    remaining = 1 - cost
    change_returned = []
    for coin in coin_list:
        num_coins,remaining = divmod(remaining,coin)
        change_returned.append(int(num_coins))
    print(" Q"," D ","N ","P")
    return change_returned

# The float version has trouble with round errors,
# it doesn't give proper penny change



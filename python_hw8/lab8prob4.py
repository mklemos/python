# Maximilian Lemos
# Lab 8 problem 4
    
first4 = set([1,2,3,4])
every2 = set([2,4,6,8])

union = first4 | every2
intersection = first4 & every2
relative_comp = every2 - first4

print(type(first4),first4)
print(type(every2), every2)
print(type(union), union)
print(type(intersection), intersection)
print(type(relative_comp), relative_comp)




li = [1, 9, 8, 4]

#basic list comp:
print([elem for elem in li])

#basic math applied, multiply each element in the list by two
print([elem*2 for elem in li])


#list comp with applied iterator:
i = 0
while i < 10:
    i = i + 1
    print([elem*i for elem in li])

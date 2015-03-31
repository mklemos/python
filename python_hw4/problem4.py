# Problem 4
# Maximilian Lemos

# This is the starting string seperated by commas:
test_list = "fred,a4b7,alice,cc3c,joan,3arm,todd,warm"

# Using zip to combine the split list, this is indicating that
# the odd items split by commas are seen as the keys and the values
# that are even are seen as the values in the newly created dictionary.

helper_list = test_list.split(',')

# Here are the keys in a list:
print("The Keys:")
dakeys = helper_list[0::2]
print(helper_list[0::2])
print('\n')

# Here are the values in a list:
print("The Values:")
davalues = helper_list[1::2]
print(helper_list[1::2])
print('\n')

#zip fxn to throw them together:
zipdakeys = zip(dakeys, davalues)


# Putting them together into the dictionary:
print("Combining the keys with the values:")
final_dict = dict((a,b) for a,b in zipdakeys)
print(final_dict)


print("--------using .keys(), .values(), and .items()--------")


print(final_dict.keys())
print(final_dict.values())
print(final_dict.items())

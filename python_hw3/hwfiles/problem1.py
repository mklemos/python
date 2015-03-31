# Maximilian Lemos
# Problem 1
# 02-04-15

user_input = input("Please input a series of numbers as a \n string (seperated by commas do not use spaces): ")
print("\nAnswers:")
print("Original string: ",user_input, "\nType confirmation: ", type(user_input),"\n")
new_list = user_input.split(",")
print("String in list form: ", new_list)
print("Length of List: ", len(new_list))

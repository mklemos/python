## Maximilian Lemos
## HW2, Problem5
## 01/29/15

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
start = 0
stop = 0

user_input = eval(input("Please enter the number of the month you'd like to see: "))

print("You chose: ",user_input)

if user_input <= 12:
    stop = (user_input * 3)
    start = stop - 3
    print(months[start:stop])



    

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
monthValue = 5
startMonth = 0
endMonth = 0

if monthValue <= 12:
    print(monthValue)
    endMonth = (monthValue * 3)
    startMonth = endMonth - 3
    print(months[startMonth:endMonth])
    
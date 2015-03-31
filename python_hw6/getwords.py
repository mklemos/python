def getwords():
    name = input("Filename Please: ")
    filein = open(name, 'r')
    mystring = ""

    for i in filein:
        mystring = mystring + i.strip() + " "
    mystring = mystring.strip()

    helper_list = mystring.split(" ")
    dakeys = helper_list[0::2]
    davalues = helper_list[1::2]
    zipdakeys = zip(dakeys, davalues)
    final_dict = dict((a,b) for a,b in zipdakeys)
    print(final_dict)
    return final_dict

def control_flow():
    import sys
    dictionary = getwords()
    keys = dictionary.keys()
    values = dictionary.values()
    username = input("Please input a username: ")
    password = input("Please input a password: ")
    while username == 'z':
        print("You entered z, goodbye.\n")
        sys.exit()
        
    while username in keys and password in values:
            while username == 'Bob' and password == 'x47y':
                print("Correct, welcome Bob.\n")
                control_flow()
            while username == 'Jane' and password == 'aa3a':
                print("Correct, welcome Jane.\n")
                control_flow()
            while username == 'Sue' and  password == '4eff':
                print("Correct, welcome Sue.\n")
                control_flow()
            while username == 'John' and  password == 'crow':
                print("Correct, welcome John.\n")
                control_flow()
            break
    while username not in keys:
            print("Try again. User does not exist.\n")
            control_flow()
    while password not in values:
            print("Try again. Invalid password. \n")
            control_flow()


control_flow()


##    while username == 'z':
##        print("Goodbye. Ending.")
##        break
##        break

        
##    for i in keystemp = dictionary.get(i)
##        if temp:
##            print (temp)
##            break



##    username = input("Please input a username: ")
##    while username != 'z':
##        password = input("Please input a password: ")
##        if username in dictionary:
##            while password == 'x47y':
##                print("Correct - Bob")
##                break
##            while password == 'aa3a':
##                print("Correct - Jane")
##                break
##            while password == '4eff':
##                print("Correct - Sue")
##                break
##            while password == 'crow':
##                print("Correct - John")
##                break`
##    username = input("Please input a username: ")
##    password = input("Please input a password: ")
##    while username != 'z':
##        while username in keys and password in values:
##            while password == 'x47y':
##                 print("Correct - Bob")
##                 break
##            while password == 'aa3a':
##                 print("Correct - Jane")
##                 break
##            while password == '4eff':
##                print("Correct - Sue")
##                break
##            while password == 'crow':
##                print("Correct - John")
##                break
##            break
##        while username not in keys or password not in values:
##            print("Try again.\n")
##            break
##        validity()



# Lab 7 problem 1
# Maximilian Lemos

def parts():
        outfile=open("parts.txt",'w')
        prompt = input("Please enter an item, quantity, and price seperated by a single space: ")
        while prompt != '!':
        #for i in range(4):
                outfile.write(str(prompt)+'\n')
                prompt = input("Please enter an item, quantity, and price seperated by a single space: ")

        print("Thanks, all done.")
        outfile.close()




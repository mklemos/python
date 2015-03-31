def storefib():
        one=two=1
        outfile=open("fib10.txt",'w')
        for i in range(10):
                if i < 2:
                        outfile.write(str(one)+'\n')
                else: 
                        result = one + two
                        outfile.write(str(result)+'\n')
                        one = two
                        two = result
        outfile.close()

##
##def getfib():
##        infile = open('fib10.txt','r')
##        for value in infile:
##                number = int(value)

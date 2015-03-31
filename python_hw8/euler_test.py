##n = 0
##for i in range(1,100):
##    if not i % 5 or not i % 3:
##        n = n + i
##        print('iterator: ',i," total: ",n)
##print('total: ',n)

n=0.0
for i in range(1,100):
    if i % 5.0: ##or i % 3.0:
        n = n + i
        print('iterator: ',i," total: ",n)
print(n)
        

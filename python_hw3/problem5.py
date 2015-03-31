## Lab3 problem5
## Maximilian Lemos
## 02-04-2015

avlist = [23,34,12,56,78,34,22,91,17,26,33]
listlen = len(avlist)
print ("Length of list: ",listlen)
sumlist = sum(avlist)
mean = sumlist/listlen

print("The mean is: ", mean)

avlist.sort()
print ("The median is: ", avlist[listlen//2])

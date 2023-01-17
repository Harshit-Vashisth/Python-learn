def swaps(l):
    i=0
    while i+1<len(l):
        #swaping in pyhton is like this
        l[i],l[i+1]=l[i+1],l[i]
        i=i+2

l=[2,1,4,3,6,5]
swaps(l)
print(l)
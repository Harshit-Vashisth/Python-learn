l=[int(i) for i in input().split()]
for i in range(len(l)):
    if(i==0 and l[i]>l[i+1]):
        print(l[i])
    elif (i == len(l)-1 and l[i] > l[i - 1]):
        print(l[i])
    elif (  l[i] > l[i - 1]  and l[i]>l[i+1]  ):
        print(l[i])

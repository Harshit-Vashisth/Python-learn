def print_array(a):
    l1=[]
    l2=[]
    l3=[]
    for i in range( 1,a+1):
        if(i%2==0):
            l2.append(i)
        else:
            l1.append(i)
    for i in l1:
        l3.append(i)
    for i in range(len(l2)-1,-1,-1):
        l3.append(l2[i])
    print(l3)





n=int(input())
for i in range(n):
    print(print_array(int(input())))
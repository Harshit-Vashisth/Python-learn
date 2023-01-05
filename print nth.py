n =int(input())
a=5
c=0
for i in range(1,n*4,1):
    if (3*i+2)%4!=0:
        print(3*i+2)
        c=c+1
        if(c==n):
            break

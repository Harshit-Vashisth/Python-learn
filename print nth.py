n =int(input())
a=5
c=0
for i in range(1,n*4,1):
    if (3*i+2)%4!=0:
        print(3*i+2)
        c=c+1
        if(c==n):
            break

#check if numbe is prime
n=int(input())
flag=False
for i in range(2,n,1):
    if(n%i==0):
        flag=True
if(flag!=True):
    print("Prime")
else:
    print("No ")

#patttern using for
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for s in range( i,2*i,1):
        print(s,end=" ")
    for z in range(2*i-2,i-1,-1):
        print(z,end="")
    print()
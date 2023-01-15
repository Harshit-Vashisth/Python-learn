def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input())
r=int(input())
print(fact(n)//(fact(r)*fact(n-r)))
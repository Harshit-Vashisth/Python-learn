def check(n):
    a=0
    b=1
    while(b<=n):
        if(b==n or a==n):
            return True
        t=a
        a=b
        b=t+b
    return False

n=int(input())
print(check(n))

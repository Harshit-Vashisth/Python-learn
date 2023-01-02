num=int(input())
ans=0
while num>0:
    n=num%10
    ans=ans*10+n
    num=num//10
print(ans)
nu=int(input())
num=nu
ans=0
while num>0:
    n=num%10
    ans=ans*10+n
    num=num//10
if nu==ans :
    print("yes")
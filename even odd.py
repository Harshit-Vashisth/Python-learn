a=int(input())
ans1=0
while a>0 :
    n=a%10
    if n%2==0 :
        ans1+=n
    a=a//10
print(ans1)
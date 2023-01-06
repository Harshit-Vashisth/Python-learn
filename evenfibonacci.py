n2=1
n1=0
sum=0
n=int(input())
while n2<n:
    if n2%2!=0:
        sum=sum+n2
    k=n1
    n1=n2
    n2=k+n2
print(sum)

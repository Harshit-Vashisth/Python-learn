n=int(input())
count=0
n1=0
n2=1
while count<n :
    ans=n2
    k=n1
    n1=n2
    n2=n1+k
    count=count+1
print(ans)

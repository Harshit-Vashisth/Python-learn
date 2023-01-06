n2=1
i=1
sum=1
n=int(input())
while i<n+1:
    sum=sum*i
    i=i+1
count=0
n=sum
while n!=0:
    a=n%10
    if(a!=0):
        break
    count =count+1
    n=n//10;

print(count)
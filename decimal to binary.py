n=int(input())
s=0
while n>=1:
    a=n%2
    s=s*10+a
    n=n//2

s1=0
while s!=0:
    a=s%10
    s1=s1*10+a
    s=s//10
print(s1)
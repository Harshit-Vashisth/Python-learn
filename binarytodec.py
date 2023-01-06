n=int(input())
i=0
num=0
s1=0
while n!=0:
    a=n%10
    num=num+(2**i)*a;
    n=n//10
    i=i+1
print(num)
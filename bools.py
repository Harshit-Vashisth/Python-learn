a=True
b=False
print(a)
print(b)
c="Ninjas"
#only True not true or false
type(c)
type(a)

#iF else

a=True
if a:
    print("harshit")
    print("Sataskhi")
else:
    print("I am in else")

 #check odd or even

k=int(input())
r=k%2
if r==0:
    print("even")
else:
    print("odd")
print("if u dont want u can skip else part also ")

#7
a=4
b=5
c=9
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)

#write a program to check +ve -ve 0
no=int(input())
if no>0 :
    print("+ve")
elif no<0:
    print("-ve")
else:
    print("zero")

#write a prog to prnit odd even and check %3 1
num=int(input())
if num%2==0 :
    print("even")
    if num/3==0 :
        print("yup")
else:
    print("ODD h bro ")

    ##while loop
#print 1 to num
c=1
while c<=num :
    print(c)
    c=c+1

#print sum from 1 to num
k=1
ans=0
while k<=num:
    ans=ans+k
    k=k+1
print(ans)

#only the even digit sum
k=2
ans=0
while k<=num:
    ans=ans+k
    k=k+2
print(ans)

#prime numbers or not
c=2
k=0
while c<num :
    if num%c==0 :
        k=k+1
    c=c+1
if k>0:
    print("no")
num=9
##nested while
c=2

print("HIH")
while c<=num :
    k=0
    f=2
    while f<c :
        if c%f==0 :
            k=k+1
        f=f+1
    if k==0:
        print(c)
    c=c+1


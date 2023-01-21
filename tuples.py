a=(1,2,3,4,5)
print(a)
b=[1,2,3,4,5]
print(b)

#another way of tuple initilization
b=3,4
print(b)

print(b[1])
print(b[-2])

f=(1,2,3,4,5,6)
for i in f:
    print(i)

for i in range(2,6) :
    print(f[i])

print(4 in b)

print(len(f))

a=(1,2,4)
b=(3,5,7)
c=a+b
d=a,b
print(c)
print(d)

#repeatition
a=a*3
print(a)

a=(2,3)
print(max(a))
print(min(a))
b=(1,14,1.5,4,15.5)
print(min(b))
print(max(b))

#using tuple function
l=[1,2,2,3,4,5]
print(tuple(l))
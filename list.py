# ways to create a list
a=[1,2,3,4]
print(a)
a=list([1,2,3,4])
print(a)
a=list()
print(a)

#updating a list
a=[1,2,3,4]
a[2]=50
print(a)

#LIST CAN STORE ANY KIND OF DATA
a=[1,2,3,[1,2,3],"hello",True,5.5]
print(a)

## better way to create lsit
b=[i for i in range(10)]
print(b)

b=[i*i for i in range(10)]
print(b)

len(b)

a=a+b
print(a)

a*3
print(a)

a.append(10)
print(a)

b.insert(1,4)
print(b)

a.extend(b)
print(a)

a.remove(5.5)
print(a)
#actual number is remove not index
#in case of multiple time same occurance is removed

print(a.pop(5))

#sorting orignal list
a=[1,5,4,32,7]
a.sort()
print(a)
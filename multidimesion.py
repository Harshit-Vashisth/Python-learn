l=[1,2,3,4,5]
print(l[::-1])

## multidimensional list
#slcing in 2d list is same as that one
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(a[1:3])

a=[[1,2] for i in range(10)]
print(a)

a=[[0 for j in range(5)] for i in range(10)]
print(a)


## multi dimension input
print("Enter the dim")

s=input().split()
m=int(s[0])
n=int(s[1])

l=[]
for i in range (m):
    next_r=[int(i) for i in input().split()]
    l.append(next_r)
print(l)

l=[]
for i in range(m):
    next_r=[]
    for j in range(n):
        next_r.append(int(input()))
    l.append(next_r)
print(l)

a=[[j+1 for j in range(n)]for i in range (m)]
print(a)
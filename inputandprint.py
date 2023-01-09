s=int(input())
a=[]
for i in range (s):
    next=int(input())
    a.append(next)
print(a )

#or taking line inputs
l=input().split()
a=[]
for s in l:
    a.append(int(s))
print(a)

#   one line input
a=[int(s)  for s in input().split()]
print(a)
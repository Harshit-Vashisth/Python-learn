l=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

print(l)
m=len(l)
n=len(l[0])


for i in range(n):
    if i%2==0:
        for j in range(m):
            print(l[j][i],end=" ")
    else:
        for j in range(m-1,-1,-1):
            print(l[j][i],end=" ")
    print()
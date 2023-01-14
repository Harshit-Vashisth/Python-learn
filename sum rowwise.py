
def row_print(a):
    m=len(a)
    if(m==0):
        return
    for i in range (m):
        sum=0
        for j in range(5):
            sum+=a[i][j]
        print(sum)


a=[[j+1 for j in range(5)] for i in range(5)]
print(a)
print(row_print(a))

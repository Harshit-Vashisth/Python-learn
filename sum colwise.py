#sum coloumn wise

def print_col(a):
    m=len(a)
    if(m==0):
        return
    n=len(a[0])
    for i in range (m):
        sum=0
        for j in range(n):
            sum+=a[j][i]
        print(sum)

a=[[j+1 for j in range(5)]for i in range(5)]
print(a)
print(print_col(a))
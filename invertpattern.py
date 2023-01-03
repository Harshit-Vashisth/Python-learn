n=int(input())
i=0
while i<n:
    j=1
    while j<=n-i:
        print("*",end="")
        j=j+1
    print("")
    i=i+1

n=int(input())
i=0
while i<n:
    j=1
    while j<=n-i:
        print(n-i,end="")
        j=j+1
    print("")
    i=i+1

#reverse pattern
i=1
n=int(input())
while i<=n:
    j=1
    while j<=n-i :
        print(' ',end="")
        j=j+1
    z=1
    while z<=i:
        print("*",end="")
        z=z+1
    print(" ")
    i=i+1

#hw 16 reverse pattern
i=1
n=int(input())
while i<=n:
    j=1
    while j<=n-i :
        print(' ',end="")
        j=j+1
    z=1
    while z<=i:
        print(z,end="")
        z=z+1
    print(" ")
    i=i+1


##iscolelus triangle
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(' ',end=" ")
        j=j+1
    z=1
    while z<=i:
        print(z,end=" ")
        z=z+1
    k=i-1
    while k>=1:
        print(k,end=" ")
        k=k-1
    print(" ")
    i=i+1

##18 hw iscolelus triangle
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(' ',end=" ")
        j=j+1
    z=1
    while z<=i:
        print("*",end=" ")
        z=z+1
    k=i-1
    while k>=1:
        print("*",end=" ")
        k=k-1
    print(" ")
    i=i+1

    ##19  iscolelus triangle
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(' ', end=" ")
        j = j + 1
    z = 0
    while z < i:
         print(z+i, end=" ")
         z = z + 1
    k = i - 1
    while k >= 1:
        print(k+i-1, end=" ")
        k = k - 1
    print(" ")
    i = i + 1
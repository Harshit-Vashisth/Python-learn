n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n/2-i+1:
        print(' ', end="")
        j = j + 1
    z = 1
    while z <=i and i<=n/2+1:
         print("*", end="")
         z = z + 1
    k = i - 1
    while k >= 1 and i<=n/2+1:
        print("*", end="")
        k = k - 1

    m=i-n/2
    while i>n/2+1 and m>=1:
        print(' ',end="")
        m=m-1
    l=1
    while i>n/2+1 and l<=n-i+1:
        print('*',end="")
        l=l+1
    h=1
    while i>n/2+1 and h<=n-i:
        print('*',end="")
        h=h+1
    print(" ")
    i = i + 1
#1 first pattern
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print("")
    i=i+1

#second pattern
n=int(input())
i=1
while i<=n:
    j=0
    while j<i:
        print(j+i,end="")
        j=j+1
    print("")
    i=i+1

#third pattern
n=int(input())
c=1
i=1
while i<=n:
    j=1
    while j<=i:
        print(c,end="")
        j=j+1
        c=c+1
    print("")
    i=i+1

#hw pattern
n=4
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print("")
    i=i+1

#hw 2
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    print("")
    i=i+1


#reverse number pattern
n=int(input())
i=1
while i<=n:
    j=i
    while j>=1:
        print(j,end=" ")
        j=j-1
    print(" ")
    i=i+1

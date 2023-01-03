n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print(chr(ord('A')+j-1),end="")
        j=j+1
    print(" ")
    i=i+1

n=int(input())
i=0
while i<n:
    j=1
    while j<=n:
        print(chr(ord('A')+j-1+i),end="")
        j=j+1
    print(" ")
    i=i+1

n=int(input())
i=0
while i<n:
    j=1
    while j<=n:
        print(chr(ord('A')+i),end="")
        j=j+1
    print(" ")
    i=i+1

#10 hw pattern
n=int(input())
i=0
while i<n:
    j=0
    while j<=i:
        print(chr(ord('A')+i),end="")
        j=j+1
    print(" ")
    i=i+1
#11 hw pattern
n=int(input())
i=0
while i<n:
    j=0
    while j<=i:
        print(chr(ord('A')+j+i),end="")
        j=j+1
    print(" ")
    i=i+1

#12 hw pattern
n=int(input())
i=0
while i<n:
    j=0
    while j<=i:
        print(chr(ord('A')+n-i+j-1),end="")
        j=j+1
    print(" ")
    i=i+1





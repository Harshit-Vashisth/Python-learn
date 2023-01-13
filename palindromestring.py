n=input()
i=len(n)
c=n[0]
k=n[i:0:-1]+c
print(k)
if(n==k):
    print("yes they are same")
for i in range( 1,10,1):
    if(i==6):
        break
    print(i)
    i=i+1

    #square integral
ans=0
n=int(input())
for i in range(1,n,1):
    if i*i<=n:
        ans=i;
print(ans)

##continue use to skip particuler itteration

for i in range(1,10):
    if i==5:
        continue
    print(i)
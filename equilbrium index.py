l=[int(s) for s in input().split()]
sum1=0
for i in l:
    sum1+=i
sum2=0
for i in range(0,len(l),1):
    sum1-=l[i]
    if(sum1==sum2):
        print(i)
        break
    if i==len(l)-1:
        print('-1')
    sum2 += l[i]

#l1=[int(i) for i in input().split()]
l1=[1,5,10,15,20,25]
l2= [2,4,5,9,15]
#l2=[int(i) for i in input().split()]

sum=0
sum1=0
sum2=0
j=0
i=0
while i<len(l1) and j<len(l2):
    while i<len(l1) and l1[i]<l2[j]:
        sum1+=l1[i]
        i+=1
    while j<len(l2) and l2[j]<l1[i]:
        sum2+=l2[j]
        j+=1
    if(l1[i]==l2[j]):
        sum1+=l1[i]
        sum2+=l2[j]
        sum+=max(sum1,sum2)
        i+=1
        j+=1
        sum1=0
        sum2=0

while( i <len(l1)):
    sum1+=l1[i]
    i+=1
while( j <len(l2)):
    sum2+=l2[i]
    j+=1
sum+=max(sum1,sum2)
print(sum)





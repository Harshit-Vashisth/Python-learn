for i in range(5):
    print(i,end='')
print(" ")

for i in range(1,5):
    print(i,end='')
print(" ")

for i in range(1,6,1):
    print(i,end='')
print(" ")

for i in range(1,5,2):
    print(i,end='')
print(" ")

a=int(input())
b=int(input())
if a%3==0 :
    s=a
elif a%3==1:
    s=a+2
else:
    s=a+1
for i in range(s,b,3):
    print(i,end='')
print(" ")
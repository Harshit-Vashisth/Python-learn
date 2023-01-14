s=input()

l=s.split(" ")
print(l)
k=""
for i in l:
    k+=i[::-1]+' '

print(k)
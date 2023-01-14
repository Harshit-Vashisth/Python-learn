s=input()
print(s)

##*******

k=""
v=0
c=""
for i in range(len(s)):
    if(c!=s[i]):
        c=s[i]
        k+=s[i]
        v+=1

print(k)
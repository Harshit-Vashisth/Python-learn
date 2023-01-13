#replace onceeee

s=input()
i=s.find('x')
if(i!=-1):
    s=s[:i]+'y'+s[i+1:]
print(s)

s=input()

for i in range(0,len(s)):#len is used for lenght
    if(s[i]=='x'):
        s=s[:i]+'y'+s[i+1:]
print(s)
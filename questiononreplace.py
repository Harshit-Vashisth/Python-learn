#replace onceeee

s=input()
i=s.find('x')
if(i!=-1):
    s=s[:i]+'y'+s[i+1:]
print(s)
l=[0 for j in range (26)]
s=input()
for i in range(len(s)):
    l[ord(s[i])-ord('a')]+=1;
    max=0
    ans=0
for i in range(len(l)):
    if(l[i]>max):
        max=l[i];
        ans=i;

print(chr(97+ans))
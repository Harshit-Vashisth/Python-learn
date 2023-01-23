def maxdis(s):
    ans=0
    max=0
    d={}
    for w in range(0,len(s)):
        if d.get(s[w],0)>w:
            d[s[w]]=d.get(s[w],0)-w
        else:
            d[s[w]]=w
    for w in d:
        if (d[w]>max):
            ans=d[w]
            max=d[w]
    return ans

s=[1,3,1,4,5,6,4,8,3]
print(maxdis(s)-1)
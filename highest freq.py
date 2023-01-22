def printwords(s):
    ans=0
    max=0
    d={}
    for w in s :
        d[w]=d.get(w,0)+1
    for w in d:
        if(d[w]>max):
            ans=w
            max=d[w]
    return ans

s=[1,2,2,3,2,2,3,4,5,6,8,4,0,1,1,2,4,4,4,4,4,4,4,4,4,4]
print(printwords(s))
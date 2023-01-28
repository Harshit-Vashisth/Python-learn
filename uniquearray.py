l=[1,2,3,4,4,1,6]
def unique(l):
    s=set()
    for i in l:
        s.add(i)
    return len(l)-len(s)

count=unique(l)
print(count)
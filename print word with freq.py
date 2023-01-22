def printwords(s,n):
    d={}
    word=s.split()
    for w in word :
        d[w]=d.get(w,0)+1
    for w in d:
        if(d[w]==n):
            print(w)

s="Harshit is a very very is goof boy "
printwords(s,2)
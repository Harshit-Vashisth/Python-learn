a=20
def f1():
    a=3
    print(f1)
f1()
print(a)

def f3():
    global a
    a=21
f3()
print(a)

def f4():
    a=30
    return a
print(a)
g=f4()
print(g)

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

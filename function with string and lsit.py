
def listing(a):
    a[0]=a[0]+1

a=[1,2,3]
listing(a)
print(a)
##but if
def listing(a):
    a=[3,4,5]

a=[1,2,3]
listing(a)
print(a)

#list does not change in case of string they are mutable so we dont need to do anything
##string will be alwasy created new they cant be modified


def sum(a,b,c=0):
    return a+b+c
print(sum(3,4))
print(sum(3,4,4))

#what if i can use as many inputs i want to use

def sum(a,b,*more):#if i dont put extra parameters apart form a and b it will be an empty tuple
    #here the more is a tuple which means we can add so many parameters and can acess them using for loop
    sum=0
    for i in more:
        sum+=i
    sum+=a+b
    return sum
print(sum(3,4))
print(sum(1,2,3,4,5,6,7,8,9,10))

## diffreent values to be return together like
def sum(a,b):
    return a*b,a+b

a,b=sum(4,5)
#either the values to retrun and store like a and b be same or u can just use one varible the values input will be in the form of  tuples

#like

a=sum(5,6)
print(a)
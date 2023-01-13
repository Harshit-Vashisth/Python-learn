a="hello"
b="harshit"
print(a+b)
#or
# a=a+b
print(a)

#it get concatinate note new string named helloharshit is created not the orginal string is change

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)
print(a==b)


###############################

##LOWER CASE AND UPPER CASE

a="this is a string "
a=a.upper()
print (a)
a=a.lower()
print(a)

print(a.isupper())
print(a.islower())


########
####  use of split function

a="this is a string "
a=a.split()
print(a)

#u can also specify spilt acc to yourself
a="this is a string "
a=a.split("is")
print(a)

#replace a particular phrase
a="this is a string"
a=a.replace("is","are")
print(a)

#finding a pharse
print(a.find("are"))

## check if a is alpha batically
print(a.isalpha())
#space is not an alphabet there its false

#check if startwith

print(a.startswith("th"))


#check endwith
print(a.endswith("g"))


####################################
## string slicing
a="this is a string"
print(a[2])  ##  give one char

print(a[3:10]) # 3 is the starting 10 is the end ... but the output will be from 3 to 9 ie start to end -1

print(a[2:])## 2 to end

print(a[:5])  ## start to 5-1

print(a[1: 10: 2])## with a gap of 3

print(a[10:1:-1])  #print them in  rev order



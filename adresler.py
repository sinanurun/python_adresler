a=10
b=11
c=12
print(a is c)      False
print(a is not b)  True
a+=1
print(a is b)      True
a+=1
print(a is c)      True

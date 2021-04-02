import collections
from collections import namedtuple,Counter
point=namedtuple('Point','xa y z')
p1=point(3,4,5)
print(p1)
# print(Counter(p1))
#Using a list as a parameter
point2=namedtuple('Point',['a','b','c'])#name of the class & the Parameters
p2=point2(7,8,9)
print(p2)
#Using a tuple as a parameter
point3=namedtuple("Point",('m','n','o'))
p3=point3(1,2,3)
print(p3)
#Using a dictionary
point4=namedtuple('Point',{'k':5,'l':0,'m':0 })
p4=point4(10,11,12)
print(p4)
print(p4.k)#Accessing the named  tuples
print(p4[1])
print(p4._fields) #Getting all the fields
p4=p4._replace(k=15)#Changing the values of the tuple
print(p4)
p5=point4._make(['a','b','c'])
print(p5)



import collections
from collections import Counter
#counter
#deque
#namedTuple()
#orderDict
#defaultdict
c=Counter('Jamiee')
print(c)
l=Counter(['a','b','c','c'])
print(l)
print(l['c'])
f=Counter({'a':1,
           'b':2
           })
print(f)
print(f['a'])
print(list(f.elements()))
p=Counter(cats=4,dogs=7)
print(p)
print(p['cats'])
print(p['pet'])#Returns zero because pet does not exists
print(list(p.elements()))#Prints all the elements in the Counter function
print(p.most_common())
#New Counter
z=Counter(a=4,b=2,c=0,d=-2)
l=['a','b','b','c']
z.subtract(l)
print(z)
z.update(l)
print(z)
z.clear()
print(z)
#Addition,Substaction, Intersection and Union of counters
m=Counter(a=4,b=2,c=0,d=-2)
n=Counter(['a','b','b','c'])
print(m+n)
print(m-n)

print(m&n)#Intersection
print(m|n)#Union
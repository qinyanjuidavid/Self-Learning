import collections
from collections import deque
#deque is similar to list
d=deque("hello")
print(d)
#appending
d.append("world")
print(d)
d.appendleft("....")
print(d)
#poping removes the last element in the deque
d.pop()
print(d)
d.pop()
print(d)
#pop can also work from the left hand side
d.popleft()
print(d)
#clear removes all the elements in the deque
d.clear()
print(d)
#append
d.append('world')
print(d)
#Inserting in the deque
d.insert(0,'hello')
print(d)
print(len(d))
l=deque('1234')
print(l)
d.extend(l)
print(d)
#Extend left reverses the deque
a=deque('abcd')#arranged as dcba
print(a)
#Thus this deque must be reversed again inorder for it to appear in the required formart
a.reverse()
d.extendleft(a)
print(d)
print(d.count(d))
#rotate method
print(d)
d.rotate(-1)
print(d)
d.rotate(-2)
print(d)
print(d.rotate(2))
print(d)

#mxLength
l=deque('hello',maxlen=5)
print(l)
l.append('w')
print(l)
l.append('o')
l.append('r')
l.append('l')
l.append('d')
print(l)
print(l.maxlen)
# l.maxlen=6 The maxlength cant be changed, once initiated
print(l)


x=[i**2 for i in range(1000)]
for el in x:
    print(el)
#This fills up our RAM
class Gen:
    def __init__(self,n):
        self.n=n
        self.last=0
    def __next__(self):
        return self.next()
    def next(self):
        if self.last==self.n:
            raise StopIteration()
        rv=self.last**2
        self.last+=1
        return rv
g=Gen(1000)
while True:
    try:
        print(next(g))
    except StopIteration:
        break
#Generators
def gen(n):
    for i in range(n):
        yield i**2
g=gen(1000)
for i in g:
    print(i)
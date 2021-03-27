from time import sleep
class Compute:
    # def __call__(self, *args, **kwargs):
    #     rv=[]
    #     for i in range(10000):
    #         sleep(5)
    #         rv.append(i)
    #     return rv
    def __iter__(self):
        self.last=0
        return self
    def __next__(self):
        rv=self.last
        self.last+=1
        if self.last>10:
            raise StopIteration
        sleep(.1)
        return rv
l=[]
for val in Compute():
    print(val)
    l.append(val)
print(l)

#Generator
def compute():
    for i in range(0,-10,-1):
        sleep(.5)
        yield i
rv=[]
for val in compute():
    print(val)
    rv.append(val)
print(rv)
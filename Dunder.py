import inspect
from queue import Queue
x=[1,2,3]
y=[4,5]
print(x+y)
print(len(x+y))
print(x*5)
print(x.index(2))
#Lets get into dunder
class Person:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "Person: {}".format(self.name)
    __repr__=__str__
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid arguments, X must be an integer.")
        self.name=self.name*x
        return self.name
    def __call__(self,y):
        print("Called this function {}".format(y))
    def __len__(self):
        return len(self.name)
p1=Person("Jamie")
print(p1)
p2=p1*5
print(p2)
p1(5)
print(len(p1))

q=Queue()
print(q)
print(inspect.getsource(Queue))
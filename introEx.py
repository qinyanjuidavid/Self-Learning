import inspect
class Dog:
    def __init__(self):
        self.bark()
#Python usually checks if the syntax is valid
#python is a run time language and not a complier time language
def make_class(x):
    class Dog:
        def __init__(self,name):
            self.name=name
        def print_value(self):
            print(x)
    return Dog
m1=make_class(10)
d=m1("Angie")
d.print_value()
#For loop
for i in range(10):
    def show():
        print(i*2)
    show()
#Functions inside the functions
def func(x):
    if x==1:
        def rv():
            print("X is equal to 1.")
    else:
        def rv():
            print("X is not 1.")
    return rv
n=func(5)
n()
l=func(1)
l()
print(id(l()))#Memory
print(inspect.getmembers(l))
print(inspect.getsource(l))
print(inspect.getfile(l))
#Everything in python happens live

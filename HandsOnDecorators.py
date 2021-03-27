from time import time
def add(x,y=10):
    before=time()
    sum=x+y
    after=time()
    elp=after-before
    print("Elapsed:", elp)
    return sum

print(add(10,20))
print(add.__name__)#What is the name of the module
print(add.__module__)#What type of module is it
print(add.__defaults__)#The default values
print(add.__code__)
print(add.__code__.co_code)
print(add.__code__.co_nlocals)#Number of local values
print(add.__code__.co_varnames)#The variables that the function interacts with
from inspect import getsource,getfile
print(getsource(add)) #It displays the source codes
print(getfile(add)) #The location of the script

#Lets get to the real stuff
def timer(func):
    def f(*args,**kwargs):#Wrap a function
        before=time()
        rv=func(*args,**kwargs)
        after=time()
        print("Elapse time:",after-before)
        return rv
    return f
def ntimes(n):
    def inner(f):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                print("Running {.__name__}".format(f))
                rv=f(*args,**kwargs)
            return rv
        return wrapper
    return inner
# @timer#The decorator is here with us
@ntimes(2)
def Add(x,y):
    return x+y
# @timer
@ntimes(5) #High level decorators
def Sub(x,y):
    return x-y

print(Add(10,5))
print(Sub(10,5))
#Simple syntax
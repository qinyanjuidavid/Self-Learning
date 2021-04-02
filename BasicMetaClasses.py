class Test:
    pass
print(Test)
print(Test())
print(type(Test()))
def func():
    pass
print(type(func))
#Another way of creating a class
Test=type('Test',(),{"x":5
})
print(Test)
print(type(Test))
t=Test()
print(t.x)
#Trial
class Foo:
    def show(self):
        print("hi")
def add_attribute(self):
    self.z=9
    return self.z
cls2=type("Foo1",(),{"add_attribute":add_attribute})#Adding functions
n=type("FooFoo",(Foo,cls2),{})
n1=n()
n1.show()
print(n1.add_attribute())
def OutputFeatures(self,name,age):
    return "my name is {}, I am {} years old".format(name,age)
features=type("Features",(),{"OutputFeatures":OutputFeatures})
def Color(self,color):
    return "I am {} in color.".format(color)
dog=type("Dog",(features,),{"Color":Color})
d1=dog()
print(d1.OutputFeatures("Jamie",3))
print(d1.Color("Brown"))

#Hands on MetaClasses
class Meta(type):
    def __new__(self,cls,bases,attrs):#New is called before the init method
        print(attrs)
        a={}
        for name,val in attrs.items():
            if name.startswith("__"):
                a[name]=val
            else:
                a[name.upper()]=val
        print(a)
        return type(cls,bases,a)

class Dog(metaclass=Meta):
    x=5
    y=8
    def hello(self):
        print("Hi")
d=Dog()
d.HELLO()#The function was changed to Capital letters


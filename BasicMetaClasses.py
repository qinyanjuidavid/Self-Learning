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
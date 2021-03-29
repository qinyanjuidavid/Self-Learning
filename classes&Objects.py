#Objects
x=5
y="string"
print(type(x))#Everything in Python is an objec
print(type(y))
print(help(str))
#Functions
def func(x=5):
    return x+1
print(func())
#Methods are called using .
name="John Doe"
#name is an object
print(name.upper())#Method
print(name.replace('John','Jane'))

#Classes
class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("Hi i am {}, and i am {} years old.".format(self.name,self.age))
    def changeAge(self,age):
        self.age=age
    def addWeight(self,weight):
        self.weight=weight
if __name__=="__main__":
    d1=Dog("Jamie",3)
    d1.speak()
    d2=Dog("Angie",2)
    d2.speak()
    d2.changeAge(3)
    d1.changeAge(4)
    d1.speak()
    d2.speak()
    print(d1.name)
    print(d1.age)
    print(d2.name)
    dog=[Dog('cain',5),Dog('Super',2)]
    dog[1].speak()
    print(dog[0].name)
    print(dog[0].age)
    dog[0].addWeight(6)
    print(dog[0].weight)
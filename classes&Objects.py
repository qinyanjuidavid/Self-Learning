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

#Inheritance
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return "Hi i am {}, and i am {} years old.".format(self.name,self.age)
    def talk(self,sound="bark"):
        return "{} {}\'s".format(self.name,sound)
if __name__=="__main__":
    d1=Dog("Angie",5)
    print(d1.speak())
    print(d1.talk())

class Cat(Dog):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
    def Trial(self):
        return "{} I am also {} in color".format(super().speak(),self.color)
if __name__=="__main__":
    c1=Cat('Jamie',2,"Brown")
    print(c1.speak())
    print(c1.Trial())
    print(c1.talk("Meows"))
#Multiple Inheritances
class Vehicle:
    def __init__(self,price,gas,color):
        self.price=price
        self.gas=gas
        self.color=color
    def fillUpTank(self):
        self.gas=100
    def emptyTank(self):
        self.gas=0
    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self,speed,price,gas,color):
        super().__init__(price,gas,color)
        self.speed=speed
    def beep(self):
        print("Beep beep")
if __name__=="__main__":
    c1=Car(120,100,5,"Yello")
class Truck(Car):
    def __init__(self,tires,price,gas,color):
        super().__init__(price,gas,color)
        self.tires=self.tires
    def beep(self):
        print("Hook Hook")
if __name__=="__main__":
    # t1=Truck()

#Overloading the python default methods
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.coords=(self.x,self.y)
    def move(self,x,y):
        self.x+=x
        self.y+=y
    def __add__(self, other):
        return self.x+other.y
if __name__=="__main__":
    p1=Point(3,5)
    p2=Point(5,6)
    print(p1+p2)
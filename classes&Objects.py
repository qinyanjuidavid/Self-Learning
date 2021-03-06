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
    pass

#Overloading the python default methods
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.coords=(self.x,self.y)
    def move(self,x,y):
        self.x+=x
        self.y+=y
    def __add__(self, other):#Addition
        return (self.x+other.x,self.y+other.y)
    def __mul__(self, other):#Multiplication
        return (self.x*other.x,self.y*other.y)
    def __sub__(self, other):#Substraction
        return (self.x-other.x,self.y-other.y)
    def __str__(self):#String method
        return "({},{})".format(self.x,self.y)
    def __gt__(self, other):#Greater than
        return self.x>other.y
    def __ge__(self,other):#Greater than or equal to
        return self.x>=other.y
    def __lt__(self, other):#Less than
        return self.x<other.y
    def __le__(self,other ):#Less than or equal to
        return self.x<=other.y
    def __eq__(self, other):#Equal to
        return self.x==other.y
    def __len__(self):
        return len(str(self.x))
if __name__=="__main__":
    p1=Point(3,5)
    p2=Point(5,6)
    print(p1+p2)
    print(p1*p2)
    print(p1-p2)
    print(p1)
    print(p2)
    print(p1>p2)
    print(p1>=p2)
    print(p1<p2)
    print(p1<=p2)
    print(p1==p2)
    print(len(p1))

#Class Methods, Class Variables,static method
class Dog:
    dogs=[]
    def __init__(self,name):
        self.name=name
        self.dogs.append(self)
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)
    @staticmethod
    def bark(n):
        for i in range(n):
            print("Bark!")
    def __str__(self):
        return "{}".format(self.name)
if __name__=="__main__":
    d1=Dog("Jamie")
    d2=Dog("Angie")
    print(d1.num_dogs)
    d1.bark(5)
    print(Dog.dogs)
    print(Dog.num_dogs)
    #Static Variables
    Dog.bark(2)

#Private classes and Public classes
class __Private:
    def __init__(self,name):
        self.name=name
if __name__=="__main__":
    pass

class NotPrivate:
    def __init__(self,name,priv):
        self.name=name
        self.__priv=priv
    def display(self):
        return "Hello"
    def __display(self):
        print(self.__priv)
    def setDisplay(self,priv):
        self.__priv=priv
    def getDisplay(self):
        return self.__priv

if __name__=="__main__":
    n1=NotPrivate("Jamie",55)
    n1.setDisplay(56)
    print(n1.getDisplay())

#Creating Classes
class Car:
    pass
if __name__=="__main__":
    ford=Car()
    honda=Car()
    audi=Car()

    ford.speed=200
    honda.speed=220
    audi.speed=250

    ford.color ="red"
    honda.color = "blue"
    audi.color = "black"
    print(ford.speed,ford.color)
    print(honda.speed,honda.color)

    ford.speed=280
    print(ford.speed)
    ford.color="Yellow"
    print(ford.speed,ford.color)

class Rectangle:
    pass

if __name__=="__main__":
    R1=Rectangle()
    R2=Rectangle()
    R1.width=20
    R1.height=30
    R2.width=40
    R2.height=20
    print("Area: ",R1.width*R1.height)
    print("Area: ",R2.width*R2.height)

#Adding methods
class Car:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color
        print(speed)
        print(color)
        print("The __init__ is called")
    def myAwesomeFunction():
        print("Awesome occurs only once")
if __name__=="__main__":
    ford=Car(200,"black")
    honda=Car(220,"blue")
    audi=Car(240,"Yellow")
    Car.myAwesomeFunction()
    print(ford.speed)
    print(ford.color)
    ford.speed="Orange"
    print(ford.speed)
    print(ford)
#Trial Two on the Rectangle class
class NewRectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width

if __name__=="__main__":
    R1=NewRectangle(20,30)
    R2=NewRectangle(10,40)
    print(f"Area of Rectangle one:",R1.height*R1.width)
    print(f"Area of Rectangle two:",R2.height*R2.width)

#Lets go deeper into this classes
class Hello:
    #There should only be one __init__method
    #Incase more than one, the last __init__ method in the program overwrites the rest
    def __init__(self,name):
        print("hello")
    def __init__(self):
        print('__init__')
if __name__=="__main__":
    h1=Hello()
#Arguments usually have a variable declared in them
#parameters usually get there variables from the object
class Hello2:
    def __init__(self,name="John Doe"):
        print(name)
if __name__=="__main__":
    h2=Hello2()
    h3=Hello2("Jane Doe")

#Using the *args and **kwargs
class Hello:
    def __init__(self,*args,**kwargs):
        pass
if __name__=="__main__":
    h4=Hello()
    h5=Hello("name","age","Salary",person1={
        "Age":23,
        "Salary":123000,
        "age":26
    }) #Kwargs can be represented in the form of dictionaries
#Back to serious Business
class HelloPerson:
    def __init__(self,name):
        self.name=name
        self.age=10#Default value
    def PrintOutPut(self):
        return f"My name is {self.name}, I am {self.age} years old"
if __name__=="__main__":
    h6=HelloPerson("Jane Doe")
    print(h6.PrintOutPut())

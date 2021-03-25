class Car:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color
    def __repr__(self):
        return f"Speed: {self.speed}\nColor: {self.color} "
    #Setter
    def setSpeed(self,value):
        self.speed=value
    #Getter
    def getSpeed(self):
        return self.speed

if __name__=="__main__":
    c1=Car(200,"black")
    print(c1)
    c1.speed=280
    c1.color="Yellow"
    print(c1)
    c1.setSpeed(450)
    print(c1.getSpeed())
    c1.speed=600
    print(c1.getSpeed())

#Example
class Hello:
    def __init__(self,name):
        self.a=10
        self._b=20
        self.__c=30

if __name__=="__main__":
    c1=Hello("Jane Doe")
    print(c1.a)
    print(c1._b)#This is a cconvention, its partially private
    # print(c1.__c) Private Variable
#Encapsulation works here
class NewCar:
    def __init__(self,speed,color):
        self.__speed=speed
        self.__color=color
    #Setter
    def setSpeed(self,value):
        self.__speed=value
    #Getter
    def getSpeed(self):
        return self.__speed
    #Setter
    def setColor(self,newColor):
        self.__color=newColor
    #Getter
    def getColor(self):
        return self.__color
if __name__=="__main__":
    c7=NewCar(100,"black")
    print(c7.getSpeed())
    c7.setSpeed(480)
    print(c7.getSpeed())
    print(c7)
    print(c7.getColor())
    c7.setColor("Orange")
    print(c7.getColor())
#Work on our rectangle
class Rectangle:
    def __init__(self,height,width):
        self.__height=height
        self.__width=width
    #setter for height
    def setHeight(self,height):
        self.__height=height
    #setter for Height
    def getHeight(self):
        return getHeight
    #Setter for width
    def setWidth(self,width):
        self.__width=width
    #Getter for width
    def getWidth(self):
        return self.__width
    def FindArea(self):
        return self.__height * self.__width
if __name__=="__main__":
    r1=Rectangle(20,23)
    print(r1.FindArea())
    r2=Rectangle(40,10)
    print(r2.FindArea())

#Inheritance and Encapsulation together
#??

class Hello:
    def __init__(self,name):
        self.a=10
        self._b=20
        self.__c=30
    #A Private variable can be accessed in its the particular class that it belongs
    def Public_method(self):
        print(self.a)
        print(self.__c)
        print("public")
if __name__=="__main__":
    h1=Hello("Jade")
    h1.Public_method()
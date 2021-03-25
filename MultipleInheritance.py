#Polygon class--> Super class
class Polygon:
    __width=None
    __height=None
    #Setter method
    def setValue(self,width,height):
        self.__width=width
        self.__height=height
    #Getter method for width
    def getWidth(self):
        return self.__width
    #Getter method for height
    def getHeight(self):
        return self.__height
#Shape class--> Super class
class Shape:
    __color=None
    #Setter Value
    def setColor(self,color):
        self.__color=color
    #Getter method for color
    def getColor(self):
        return self.__color

class Rectangle(Polygon,Shape):
    def Area(self):
        return self.getWidth()*self.getHeight()
if __name__=="__main__":
    r1=Rectangle()
    r1.setValue(10,20)
    print("Area of rectangle:",r1.Area())
    r1.setColor("Blue")
    print(r1.getColor())
class Triangle(Polygon,Shape):
    def Area(self):
        return (self.getHeight()*self.getWidth())/2
if __name__=="__main__":
    t1=Triangle()
    t1.setValue(12,5)
    print("Area of Triangle:",t1.Area())
    t1.setColor("Yellow")
    print(t1.getColor())


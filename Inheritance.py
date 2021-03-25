class Polygon:
    __width=None
    __height=None
    #Setter method for both width and height
    def setValues(self,width,height):
        self.__width=width
        self.__height=height
    #Getter method for width
    def getWidth(self):
        return self.__width
    #Getter method for Height
    def getHeight(self):
        return self.__height

class Rectangle(Polygon):
    def Area(self):
        return self.getWidth()*self.getHeight()
if __name__=="__main__":
    r1=Rectangle()
    r1.setValues(50,40)
    print(r1.Area())

class Triangle(Polygon):
    def area(self):
        return (self.getWidth()*self.getHeight())/2

if __name__=="__main__":
    t1=Triangle()
    t1.setValues(10,20)
    print(t1.area())



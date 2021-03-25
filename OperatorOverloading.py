import math
class Number:
    def __init__(self,num):
        self.num=num

if __name__=="__main__":
    n1=Number(1)
    n2=Number(2)
    # print(n1+n2) The class can't work with the positive value

class Circle:
    def __init__(self,radius):
        self.__radius=radius
    #Setter for the radius
    def setRadius(self,radius):
        self.__radius=radius
    #Getter for the radius
    def getRadius(self):
        return self.__radius
    def area(self):
        return math.pi*self.__radius**2
    def __add__(self, other):
        return Circle(self.__radius+other.__radius)
if __name__=="__main__":
    c1=Circle(3)
    print(c1.area())
    c2=Circle(2)
    c3=c1+c2
    print(c3.getRadius())#The radius of the two objects
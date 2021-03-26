from abc import ABC,abstractmethod #Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
if __name__=="__main__":
    pass
#Instantiation should not work
#Even one decoractor makes the abstract class
class Square(Shape):
    def __init__(self,side):
        self.__side=side
    def area(self):
        return self.__side*self.__side
    def perimeter(self):#The functions from the abstract class must be recreated again
        return self.__side**4

if __name__=="__main__":
    s1=Square(5)
    print(s1.area())
    print(s1.perimeter())
#You can not instanciate the abstract class
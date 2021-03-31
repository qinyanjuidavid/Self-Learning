class Base:
    def __init__(self):
        self.__a=10
    #Setter
    def SetA(self,value):
        self__a=value
    #Getter
    def GetA(self):
        return self.__a
if __name__=="__main__":
    b1=Base()
    print(b1.GetA())
class Derived(Base):
    def __init__(self):
        self.__b=20
        Base.__init__(self)#Calling an instance from the base class
        print(super().GetA())
    def __str__(self):
        return "Hello"
    #Setter
    def SetB(self,v):
        self.__b=v
    #Getter
    def GetB(self):
        return self.__b
    #area
    def Area(self):
#         area=self.__a*self.__b
        print(self.__b)
        
if __name__=="__main__":
    d1=Derived()
    print(d1)
    d1.Area()
    
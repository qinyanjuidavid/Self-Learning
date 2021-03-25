class Hello:
    def __init__(self,name):
        self.a=10
        self._b=20
        self.__c=30
    def PublicMethod(self):
        print(self.a)
        print(self.__c)
        print("Public")
        self.__privateMethod()#Accessing a private method
    def __privateMethod(self):
        print("I am Private")

if __name__=="__main__":
    h1=Hello("Jane")
    h1.PublicMethod()
    # h1.__privateMethod()
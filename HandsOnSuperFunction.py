class Parent:
    def __init__(self,name):
        print("Parent __init__",name)
class Parent2:
    def __init__(self,name):
        print("Parent2 __init___",name)
class Child(Parent,Parent2):
    def __init__(self):
        print("Child __init__")
        super().__init__("Max")
        Parent2.__init__(self,"Jamie")
        # Parent.__init__(self,"Jamie") #Alternative

if __name__=="__main__":
    c1=Child()
    print(Child.__mro__) #Method Resolution order-->Order in which methods are called
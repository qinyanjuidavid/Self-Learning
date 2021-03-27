from library import *

assert hasattr(Base, "foo"), "You broke it you fool!"
class Derived(Base):
    def bar(self):
        return self.foo()
if __name__=="__main__":
    d1=Derived()
    print(d1.bar())

class Derived2(Base2):
    def Bar(self):
        return "Output Bar"
if __name__=="__main__":
    d2=Derived2()
    print(d2.Bar())
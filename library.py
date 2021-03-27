class Base:
    def foo(self):
        return 'foo'
if __name__=="__main__":
    b1=Base()
    print(b1.foo())
class BaseMeta(type):
    def __new__(cls,name,bases,body):
        if name != 'Base'  and not 'bar' in body:
            raise TypeError("Bad user class")
        return super().__new__(cls,name,bases,body)

class Base2(metaclass=BaseMeta):
    def foo(self):
        return self.bar()
    def __init_subclass__(cls, *args,**kwargs):
        print("__init_subclass__",args,kwargs)
        return super().__init_subclass__(cls,*args,**kwargs)


# if __name__=="__main__":
#     b1=Base2()
#     print(b1.foo())
# #
# old_bc= __build_class__
# def my_bc(*a,**kw):
#     print("My Buildclass-->",a,kw)
#     return old_bc(*a,**kw)
# import builtins
# builtins.__build_class=my_bc
def func(x=1):#Default parameter
    return x**2
if __name__=="__main__":
    print(func(2))
    print(func(5))
    print(func())
#Exercise
def func(word,add=5,freq=1):
    return word*(freq+add)
if __name__=="__main__":
    print(func("day",5))
    print(func("John Doe"))
    print(func("Jane Doe",1,2))
#Example
class car(object):
    def __init__(self,make,model,year,condition,kms):
        self.make=make
        self.model=model
        self.year=year
        self.condition=condition
        self.kms=kms
    def display(self,showAll):
        if showAll:
            print("This car is a {} {} from {}, it is {} and has {} kms.".format(self.make,self.model,self.year,self.condition,self.kms))
        else:
            print("This car is a {} {} from {}.".format(self.make,self.model,self.year))
whip=car("Ford","Fusion",2012,"New",0)
whip.display(True)
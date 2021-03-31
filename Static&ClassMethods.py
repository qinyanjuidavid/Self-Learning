class Person(object):
    population=50
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def getPopulation(cls,y):
        return cls.population, y
    @staticmethod
    def isAdult(age):
        return age >=18
    def display(self):
        print(self.name,'is',self.age,'years old')
n1=Person("Day",18)
print(Person.getPopulation(10))#Class method
print(Person.isAdult(21))

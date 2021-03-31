#Inheritance
class Dog:
    species="Canis familiaris"
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    def __str__(self):
        return f"{self.name} a {self.breed} is {self.age} years old."
    def description(self):
        print(f"{self.name} a {self.breed} is {self.age} years old.")
    def speak(self,sound):
        return f"{self.name} says {sound}."

    
if __name__=="__main__":
    d1=Dog("Jamie",23,"Bull Dog")
    print(d1)
    d1.description()
    print(d1.speak("Woof"))


class Dog:
    species="Canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,sound):
        return f"{self.name} says {sound}"
if __name__=="__main__":
    d4=Dog("Jamie",2)
    print(d4)
class JackRusselTerrier(Dog):
    pass
if __name__=="__main__":
    d1=JackRusselTerrier("Miles",4)
    print(d1)
    print(d1.species)#The species from the parent class
    print(d1.name)#Name
    print(d1.age)#Age
    print(type(d1))
    print(type(d1.name))
    print(id(d1.age))
    print(isinstance(d1,Dog))#Checking if D1 is an instance of the Dog class
    print(isinstance(d1,JackRusselTerrier))
    print(isinstance(d1,Dachshund))

class Dachshund(Dog):
    pass
if __name__=="__main__":
    d2=Dachshund("Buddy",9)
    print(d2)
    print(d2.species)#The Species From the parent class
class Bulldog(Dog):
    pass
if __name__=="__main__":
    d3=Bulldog("Jack",3)
    print(d3)
    print(d3.species)#The species from the parent class



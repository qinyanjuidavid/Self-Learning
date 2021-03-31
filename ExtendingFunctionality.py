#Extending the functionality of the parent class
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    def speak(self,sound="Arf"):
        return f"{self.name} barks: {sound}."
    def Introduction(self):
        return f"My name is {self.name}, I am {self.age} years old."
if __name__=="__main__":
    d1=Dog("Angie",3)
    print(d1.name)
class JackRussellTerrier(Dog):
    def speak(self,sound="Arf"):
        c1=super().speak(sound) #You can access a method by the use of the super function
        print("Let\'s check this:",c1)
        return f"{self.name} barks: {sound}."
    def intro(self):
        pass
    
if __name__=="__main__":
    j1=JackRussellTerrier("Jamie",2)
    print(j1.speak())
    print(j1.intro())
    j2=JackRussellTerrier("Miles",4)
    print(j2.speak("Wuuuf"))#It replaces the default "Arf" agrument
    print(d1)#You can access the object of the parent class
    print(d1.name)
class BullDog(Dog):
    def speak(self,sound="Arf"):
        return f"{self.name} bark: {sound}."
if __name__=="__main__":
    b1=BullDog("Jim",5)
    print(b1.speak("Woof"))
    


#Exercise
class Dog:
    species="Canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    __repr__=__str__
    def speak(self,sound):
        return f"{self.name} says {sound}"
if __name__=="__main__":
    d1=Dog("Jamie",2)
    print(d1)
    print(d1.speak("Wuuf"))
class GoldenRetriever(Dog):
    def speak(self,sound="Bark"):
        return super().speak(sound)
if __name__=="__main__":
    g1=GoldenRetriever("Jamie",3)
    print(g1.speak())
        
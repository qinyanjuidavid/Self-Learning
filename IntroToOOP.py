class Dog:
    species="Canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name + f" {self.age}"
if __name__=="__main__":
    d1=Dog("Jamie",4)
    print(d1)#This is the memory where the new dog object has been created
    d2=Dog("Angie",3)
    print(d2)
    print(d1==d2)
    print(d1.name)
    print(d2.name)
    print(d1.age)
    print(d2.age)
    print(d1)#The __str__method returns the string
    print(d2)#Same here
    print(d1.species)#The class attribute can be accessed this way
    print(d2.species)
    d1.name="Buddy"
    print(d1.name)
    d1.age=10
    print(d1.age)
    d2.name="Miles"
    print(d2)


class NewDog:
    species="Canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name+f" {self.age}"
    def description(self):
        return f"{self.name} is {self.age} years old."
    def speak(self,sound):
        return f"{self.name} says {sound}"
    
if __name__=="__main__":
    d1=NewDog("Jamie",3)
    print(d1.description())
    print(d1.speak("wooof woof"))
    d2=NewDog("Miles",3)
    print(d2.description())
    print(d2.speak("woof wooof"))
    #The methods like __init__ and __str__ are called the dunder methods
    print(d2)



class Trial:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    def PrintDetails(self):
        print(f"My name is {self.name}, I am {self.age} years old.")
if __name__=="__main__":
    l1=Trial("Aggy",20)
    print(l1)
    l1.PrintDetails()
    l2=Trial("Cate",22)
    print(l2)
    l2.PrintDetails()
    

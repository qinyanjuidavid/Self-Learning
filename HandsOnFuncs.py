def addTwo(x):
    return x+2
print(addTwo(1))

def subTwo(number):
    return number-2
print(subTwo(7))
print(addTwo(6))
def printString(string):
    print(string)
printString("Hello")

def accel(mass,force):
    a=mass*force
    return a
print(accel(20,5))

def doSomething():
    print("Hello world")
    print("My name is day.")
doSomething()
#Recarp
def func(x,text):
    print(x)
    if text=="1":
        print("text is 1")
    else:
        print("text is not one")
func(5,'1')
#Argument or Adding the default value
def newFunct(n=10,y="John Doe"):
    print(f"My name is {y}.")
    return "this is number {}".format(n)
print(newFunct()) #With arguments its not a must for us to put values when calling the function
print(newFunct(19,"Jane Doe")) #We can change the default value
print(newFunct(9))

#Global and local Variables
var=9
loop=True
def func(x=5):
    global loop#Changing the global variable in the function
    newVar=7
    loop=False
    print(loop)#Local
    if x==5:
        # print(var) Global Variable it can be used anywhere in the program
        return newVar
print(func())
# print(x) x is local to the function
print(loop) #Global
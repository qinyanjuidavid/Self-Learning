for x in range(0,10):
    print(x)

for y in range(0,10,2): #Start, Stop, Increment/Step
    print(y)

for _ in range(0,-10,-1):
    print(_)

for _ in range(10):
    def Hello():
        print("Hello")
    Hello()
from time import sleep
for i in range(10):
    def multiply():
        for n in range(10):
            # sleep(.5)
            print("{}*{}= {}".format(i,n,i*n))
        # sleep(3)
        print()
    multiply()
#Iterating by Item
fruits=['apples','pears','strawberry']
for fruit in fruits:
    if fruit == "pears":
        print(fruit)
    else:
        print("not pears")

for i in range(len(fruits)):
    print("{}. I love {}.".format(i,fruits[i]))
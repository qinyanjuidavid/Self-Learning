#Check the Rectangle script in the myDirectory
#Check the Triangle Script in the myDirectory
#By Checking that it will lead you to the ModulesWithClass Script
from myDirectory.Rectangle import Rectangle
from myDirectory.Triangle import Triangle
if __name__=="__main__":
    r1=Rectangle()
    r1.setValue(10,20)
    print("Area of Rectangle:",r1.Area())

    t1=Triangle()
    t1.setValue(12,5)
    print("Area of Triangle:",t1.Area())
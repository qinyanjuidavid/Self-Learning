def firstProgram():
    theWorldisFlat=True
    if theWorldisFlat:
        print("Be carefull  not to fall off!")
    spam=1
    print(spam)
    text="#Ths is a comment because it\'s inside quotes."
    print(text)
if __name__=="__main__":
    firstProgram()

def PythonCalc():
    #Numbers
    a=2
    b=2
    sum=a+b
    print(sum)
    ans=50-5*6
    print(ans)
    ans2=ans/4
    print(ans2)
    #Division always returns a floating point number
    print(8/5)
    #Indicating the type of data type
    myint=56
    print(type(myint))
    notInt="56"
    print(type(notInt)) #This is a string
    print(id(notInt))#This indicates the memory that is allocated to the notInit Variable
    print(17/6)
    k=17
    m=3
    print(k//m) #By use of // It removes the remainder
    print(k%m) #By the use of the modulus we usually get the remainder

    #More on Variable Assignment
    width=20
    height=5*9
    area=width*height
    print(f"The area if {area}.")

    tax=12.5/100
    price=100.50
    ActualPrice=tax*price
    print(f"The Price of the shoes is {round(ActualPrice,2)} Kshs.")
if __name__=="__main__":
    PythonCalc()

def ShortProgramOnModulus():
    """ Checking if teh year is leap"""
    year=1994
    if year%4==0 and year%2==0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
if __name__=="__main__":
    ShortProgramOnModulus()
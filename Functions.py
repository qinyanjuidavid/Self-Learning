#Working with functions
def fib(n):
    """
    Printing a fibonnacci series up to n
    :param n:
    :return:
    """
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b
    print()
if __name__=="__main__":
    fib(100)

#Using a return statement in the functions
def sum(num1,num2):
    sum=num1+num2
    return sum
if __name__=="__main__":
    c=sum(10,10)
    print(c)
    print(sum(27,89))

def CheckIfPasswordIsCorrect():
    numTrials = 3
    while True:
        password="123456"
        # trial=input("Enter the password")
        trial="123456"
        if numTrials>0:
            if trial==password:
                print("Welcome Home.")
                break
            print(numTrials,"trials remaining.")
        else:
            print("Invalid Password")
            break


        numTrials-=1
if __name__=="__main__":
    CheckIfPasswordIsCorrect()

def F(a,L=[]):
    L.append(a)
    return L
if __name__=="__main__":
    print(F(1))
    print(F(2))
    print(F(45))

#Alternative
myList=[]
def myFunc(a):
    myList.append(a)
    return myList
if __name__=="__main__":
    print(myFunc(1))
    print(myFunc(3))
    print(myFunc(47))
#Upto Page 26 of the official doc python 3.7.0



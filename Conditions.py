#if Statements
def myFunct():
    # x=int(input("Please enter an integer: "))
    x=0
    if x<0:
        print("You entered a negative integer.")
    elif x==0:
        print("You entered zero.")
    elif x>0:
        print("You entered a positive integer.")
    else:
        print("This line is always printed.")
if __name__=="__main__":
    myFunct()
#for Statements
word =['cat','window','defenestrate']
for w in word:
    print(w,len(w))
word=["John","Doe","Jane Doe"]
for i in word[:]:
    if len(i)>5:
        word.insert(0,i)
print(word)

#Range Function
for i in range(5):
    print(i)
for n in range(-5,1):
    print(n)

for i in range(10):
    for n in range(i,10):
        print("*",end=" ")
    print( )
for n in range(1,100,2): #Start Value, End Value, Increment
    print(n)

#Iterating through a list
names=["Jane","Doe","Brad","John"]
for name in range(len(names)):
    print(name,names[name])
#Creating a list out of the range function
myList=list(range(90,101))
for number in range(myList[0],myList[-1],2):
    print(number)

print(myList)
print(type(myList))

#Break statements and continue statements
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"equals",x,"*",n//x)
            break
    else:
        print(f"{n} is a prime number.")

#Lets just find the number of leap years between a certain time frame
myList=list()
notLeap=[]
numOfLeapYears=0
numOfNonLeapYears=0
yearBetween=[1996,2000]
for year in range(yearBetween[0],yearBetween[-1]):
    if year%4==0 and year%2==0:
        myList.append(year)
        numOfLeapYears+=1
    else:
        notLeap.append(year)
        numOfNonLeapYears+=1
print(f"There are {numOfLeapYears} leap years between {yearBetween[0]} and {yearBetween[-1]}, these years are {myList}.")
print(f"There are {numOfNonLeapYears} non leap years between {yearBetween[0]} and {yearBetween[-1]}, these years are {notLeap}.")

#Pass Statement
while True:
    pass
class MyEmptyClass:
    pass
day=MyEmptyClass()

def iniitlog(*args):
    pass

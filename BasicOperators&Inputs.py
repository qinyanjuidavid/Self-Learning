#Basic Printing
name="Angie"
print(name)
print("Hello World")
#Inputs
print("What is your name?")
# name=input()

print("Hello {!r}".format(name))

#Operators + - / *
num1=45
num2=3
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
#Other operators **, //, %
print(64//10)
print(5%4) #Gives us remainders
num3=num1**num2
print(num3)
print(2**2)
print(num1/num2)
#Get inputs of numbers
print("Pick a number:")
num1=int(input())#use int
print("Pick another number:")
num2=eval(input())#Alternatively use eval
Sum=num1+num2
print(Sum)
def funct(x):
    return x+5
print(funct(2))
#Lambda
func=lambda x: x+3
print(func(2))

#Trial 2
fun=lambda y:"[{},{}]".format(y+2,y/3)
print(fun(1))

fun2=lambda name,age:"My name is {}, i am {} years old.".format(name,age)
print(fun2("Day",24))

fun3=lambda name,age,salary:"My name is {}, i am {} years old and i work in the {} department.".format(name,age,salary)
print(fun3("John Doe",32,"Human Resource"))
#Lambda function always gives out one return value
def myFunc(x):
    func2=lambda x: x+5
    return func2(x)+85
print(func(2))

fun3=lambda x,y=0:x+y
#In lambda you can have as many parameters or arguments as you can
#But one return type
print(fun3(5,6))
#Using map  and filter
a=[1,2,3,4,5,6,7,8,9]
n=list(map(lambda x:x+5,a))
f=list(filter(lambda x:x%2==0,a))
print(n)
print(f)
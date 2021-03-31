li=[1,2,3,4,5,6,7,8,9]
def func(x):
    return x**x
newList=[]
for i in li:
    newList.append(func(i))
print(newList)

#Using map
l=[1,2,3,4,5,6,7,8,9,10]
y=0
def func1(y):
    return y**y
print(list(map(func1,l)))
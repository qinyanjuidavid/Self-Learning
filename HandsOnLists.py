fruits=['apple','pear',1]
print(fruits)
print(type(fruits))
print(fruits[0])
fruits.append('strawberry')
print(fruits)
fruits.insert(0,"Orange")
print(fruits)
fruits.append('blueberry')
print(fruits)
fruits[-1]="Mango"
print(fruits)
fruits.reverse()
print(fruits)

#Slicing
print(fruits[0:-1:2])#Start, Stop, Step
print(fruits[0:])
print(fruits[:-1])
print(fruits[2:4])
print(fruits[::])
fruits.insert(-2,"Water melon")
print(fruits)
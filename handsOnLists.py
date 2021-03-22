square=[1,4,9,16,25]
print(square)
print(type(square)) #Checks for the data types
print(id(square))#Checks for the memory location where it is stored
#Indixing of the Lists
print(square[0])
print(square[-1])
print(square.index(25))#Checks for the index
#Slicing
print(square[0:])
print(square[:-1])
print(square[1:3])
print(len(square)) #Checks for the length of the list
square.append(64)#Adds an element to the list
print(square)
square.insert(2,3) #Adds an element to a particular index
print(square)
for i in range(len(square)):
    print(i,".",square[i])

myList=list()
for n in range(0,10):
    myList.append(n)
print(myList)
print(type(myList.index(0)))
myList[0]=11
print(myList)
#List Concatination
newList=myList+square
print(newList)
newList.pop(11)#pops a value at a cetain index
print(newList)
newList.remove(11)#Removes a particular valuea
print(newList)
#A List inside a list
awesomeList=[5,56,57,58,59]
additionalList=[4,45,46,47]
awesomeList.insert(1,additionalList)
print(awesomeList)
print(len(awesomeList))
print(awesomeList[1])
print(awesomeList[1][0])
print(type(awesomeList[1]))
letters=["a","b","c","d","e","f"]
print(letters)
newList=letters[2:5]
print(newList)
print(newList[:])#Prints all the elements in a list
grandList=[["a","b","c"],[1,2,3]]
print(grandList)
print(grandList[0])
print(grandList[1])

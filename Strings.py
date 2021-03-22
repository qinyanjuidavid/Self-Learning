print("This is my first string.")
print('This is my second string.')
def MoreOnStrings():
    myString="spam eggs"
    print(myString)
    print('doesn\'t')
    print("He\\She")
    print("\tWell said.")
    print("This is line one.\nThis is  line two.\nThis is line three.")

    print("C:\some\names")
    print(r"C:\some\names")
    print("""
This is line one.
This is line two.
This is line three
    """)
    #String Concatination
    first_name="John"
    last_name="Doe"
    print(first_name+" "+last_name)
    py="Python"
    nist="istor"
    print(py+nist)

    text=('Put several strings within parantheses'
          ' to have them joined together.')
    print(text)
    #NB:Strings can't be concatinated with integers

    #Indexing
    word="Pythonistor"
    print(word[0])#In most programming languages counting starts at zero
    print(word[-1])#This prints the last letter
    print(word[1])
    print(len(word))#Checks for the length of the string
    print(word.find("n"))#Finds and outputs the indes of n
    print(word.upper())
    print(word.lower())
    for i in range(len(word)):
        print(i,".",word[i])
    print("Hullayyy! Long process it was...")
    #String slicing
    print(word[0:6])
    print(word[6:])
    print(word[:-1])
    print(word[0:])


if __name__=="__main__":
    MoreOnStrings()
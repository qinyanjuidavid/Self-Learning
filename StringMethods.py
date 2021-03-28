#strip(), len(),lower(),upper(),split()
name="   Hello  "
print(name.strip())#It removes all the spaces in a string
nums="   1 2 3 1 4   "
print(nums.strip())#The spaces removed are before and after
print(len(name)) #Checks the length of the string
name="JOHN DOE"
print(name.lower()) #changes the strings to be in lower case
name="jane Doe"
print(name.upper()) #Changes the string to upper case
name="JOHN DOE"
print(name.split()) #Changes the string to a string
print(type(name.split()))
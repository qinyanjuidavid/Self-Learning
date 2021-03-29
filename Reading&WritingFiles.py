#Check the doc1 in the project folder
#Reading from a file
import os
file=open('doc1','r')
f=file.readlines()
l=[]
for line in f:
  l.append(line.strip())
print(l)
file.close()

#Writing to a file
file=open('file.txt','w')
file.write("Python is awesome\n")
file.write("I also love Django Framework")
file.close()

file=open("file.txt",'r')
f=file.readlines()
n=[]
for line in f:
    n.append(line.strip())
print(n)
file.close()

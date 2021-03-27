#Using or & and
x=2
y=3
if (x==y or x+y==5):
    print(":)")
else:
    print(":(")

#Nested if Statements
if x==2:
    if y==3:
        print('x={} y={}'.format(x,y))
    else:
        print('x!={}, y={!r}'.format(x,y))
else:
    print('x !={}'.format(2))
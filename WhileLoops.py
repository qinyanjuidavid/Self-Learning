x=0#Start
while x<10:#Stop
    print(x)
    x+=1#Step

password="123"
while True:
    trial=input("Enter the password:")
    if trial == password:
        print("Welcome Home...")
        break
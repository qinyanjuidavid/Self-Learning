class Customer:
    def __init__(self,name,membership_type):
        #Constructor
        self.name=name
        self.membership_type=membership_type
    def __str__(self):
        return f"{self.name} membership is {self.membership_type}."

if __name__=="__main__":
    c1=Customer("John","Bronze")
    print(c1)
    print(type(c1))
    print(id(c1))#location where it is stored
    print(c1.name)
    print(c1.membership_type)
    c2=Customer("Jane","Gold")
    print(c2)
    customers=[Customer("Doe","Bronze"),Customer("Cray","Gold")]
    print(customers[1])
    print(customers[0])
    print(customers[0].name)
    print(customers[1].membership_type)

class NewCustomer:
    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type
    def __str__(self):
        return f"{self.name} membership is {self.membership_type}."
    #Lets Change the membership
    def updateMembership(self,newMembership):
        self.membership_type=newMembership
        return newMembership
if __name__=="__main__":
    customers=[NewCustomer('Caleb',"Gold"),
               NewCustomer("Brad","Bronze")]
    customers[0].updateMembership("Platinum")#Changing the membership of Caleb
    print(customers[0])
    customers[1].updateMembership("Bronze")
    print(customers[1])#Changing the membership of Brad
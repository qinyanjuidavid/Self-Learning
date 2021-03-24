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
    def printAllCustomers(c):
        for customer in c:
            print(f"{customer.name}--> {customer.membership_type}")
    def __eq__(self, other):
        if self.name== other.name and self.membership_type==other.membership_type:
            return True
        return False
    def __repr__(self):
        return f"{self.name} has the {self.membership_type} membership."
if __name__=="__main__":
    customers=[NewCustomer('Caleb',"Gold"),
               NewCustomer("Brad","Bronze")]
    customers[0].updateMembership("Platinum")#Changing the membership of Caleb
    print(customers[0])
    customers[1].updateMembership("Bronze")
    print(customers[1])#Changing the membership of Brad
    NewCustomer.printAllCustomers(customers)
    print(customers[0]==customers[1])
    print(type(customers[0])==type(customers[1]))#Comparing the type
    print(id(customers[0])==id(customers[1]))#comparing the memory location
    print(customers) #Used for representing the entire data
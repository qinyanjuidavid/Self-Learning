class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annualSalary(self):
        return (self.pay*12)+self.bonus
if __name__=="__main__":
    s1=Salary(12000,100)


class Employee:
    def __init__(self,name,age,s1):
        self.name=name
        self.age=age
        self.salaryObj=s1
    def totalSalary(self):
        return self.salaryObj.annualSalary()
#Salary has a relationship to the employee, both can survive seperately
if __name__=="__main__":
    e1=Employee("Angie",32,s1)
    print(e1.totalSalary())
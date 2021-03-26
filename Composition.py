#Composition is delegating functions from one class
#Composition means instantiating a class in another class
class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annualSalary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.obj_salary=Salary(pay,bonus)#Composition
    def totalSalary(self):
        return self.obj_salary.annualSalary()


if __name__=="__main__":
    e1=Employee("Jamie",26,15000,50000)
    print(e1.totalSalary())
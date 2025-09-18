'''Create a class “Programmer” for storing information of few programmers 
working at Microsoft.'''

class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = programmer("Yash",120000,395004)
print(p.name,p.company,p.pincode,p.salary)
ob = programmer("Meet",100000,395007)
print(ob.name,ob.company,ob.pincode,ob.salary)
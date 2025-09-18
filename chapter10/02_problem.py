''' Write a class “Calculator” capable of finding square, cube and square root of a 
number. '''

class Calculator:
    def __init__(self,n):
        self.n = n
        
    def squre(self):
        print(f"Squre is {self.n*self.n}")
        
    def cube(self):
        print(f"Cube is {self.n*self.n*self.n}")
    
    def squreroot(self):
        print(f"Squreroot is {self.n**1/2}") 

c = Calculator(4)
c.squre()
c.cube()
c.squreroot()  
    
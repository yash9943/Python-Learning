'''Add a static method in problem 2, to greet the user with hello. '''

class Calculator:
    def __init__(self,n):
        self.n = n
        
    def squre(self):
        print(f"Squre is {self.n*self.n}")
        
    def cube(self):
        print(f"Cube is {self.n*self.n*self.n}")
    
    def squreroot(self):
        print(f"Squreroot is {self.n**1/2}") 
    
    @staticmethod
    def hello():
        print("Hello User !")

c = Calculator(4)
c.hello()
c.squre()
c.cube()
c.squreroot()  
    
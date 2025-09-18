''' Create a class (2-D vector) and use it to create another class representing a 3-D 
vector. '''

class twoDvactor:
    def __init__(self,i,j):
        self.i = i   
        self.j = j  
    
    def show(self):
        print(f"The Vactor is {self.i}i + {self.j}j.")
        
class threeDvactor(twoDvactor):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k  
    
    def show(self):
        print(f"The Vactor is {self.i}i + {self.j}j + {self.k}k.")
        
a = twoDvactor(1,2)
a.show()

b = threeDvactor(3,4,5)
b.show()
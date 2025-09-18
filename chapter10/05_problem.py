''' Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. '''

from random import randint

class train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
    
    def bookTickit(self, frm, to):
        print(f"Your tickit is booked in train no {self.trainNo} from {frm} to {to}")
        
    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time.")
    
    def getFair(self, frm, to):
        print(f"Tickit fair in train no {self.trainNo} from {frm} to {to} is {randint(222,2222)}")
        
t = train(19015)
t.bookTickit("Surat","Dwarka")
t.getStatus()
t.getFair("Surat","Dwarka")
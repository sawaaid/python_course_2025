# Ensure party.py exists in the same directory or adjust the import path accordingly
from party import PartyAnimal
 
class CricketFan(PartyAnimal): 
     points = 0 
     def six(self): 
        self.points = self.points + 6 
        self.party() 
        print(self.name,"points",self.points) 
 
s = PartyAnimal("Sally") 
s.party() 
j = CricketFan("Jim") 
j.party() 
j.six() 
print(dir(j))
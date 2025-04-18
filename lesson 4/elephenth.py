s = 'spam' 
t = list(s) 
print(t) 


s = 'pining for the fjords' 
t = s.split() 
print(t) 

s = 'spam-spam-spam' 
delimiter = '-' 
t = s.split(delimiter)
print(t)

t = ['pining', 'for', 'the', 'fjords'] 
delimiter = '-' 
print(delimiter.join(t))

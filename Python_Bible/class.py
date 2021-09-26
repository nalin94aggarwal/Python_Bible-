import random 

class pound:

 def __init__(self, rare = False):#constructor

     self.rare = rare

     if self.rare:
         self.value = 1.25
     else:
         self.value = 1.00

    
     self.color = "gold"
     self.diameter = 22
     self.thickness = 4
     self.head = True
     self.num_edged = 1

 def __del__(self):
     print("coin spent")

 
 def rust(self):
     self.color = "greenish"

 def clear(self):
     self.color = "gold"

 def flip(self):
     head_options = [True,False]
     choice = random.choice(head_options)
     self.head = choice 

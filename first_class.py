# code by 'badshasha'
# purpose : learning python oop concept 


# learning class variables : static information 

class Employee: 

    # create static varible 
    raise_amount = 1.04


    def __init__(self , first_name , secound_name , pay ) -> None:  
       self.first_name = first_name
       self.secound_name = secound_name
       self.pay = pay
    
    def fullName(self):                
        return f"{self.first_name} {self.secound_name}"  
    
    def appl_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
    
    





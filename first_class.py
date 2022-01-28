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



# create instance 
emp1 = Employee("shavendra","Ekanayake",1000)

# bad oop static variable accessible to the instance     
print(Employee.raise_amount)
print(emp1.raise_amount)


#  ===============================================================================================
#  -----------------------------------------------------------------------------------------------

# what is happen 
    # if you try to access vairable using instance 
        # 1. firts it's check the instance existing on the class instance 
        # 2. if it's not it's check the main object 

# -------------------------------------------------------------------------------------------------
# =================================================================================================


print(emp1.__dict__)
print(Employee.__dict__)
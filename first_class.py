# code by 'badshasha'
# purpose : learning python oop concept 


class Employee:  # this thing is a blue print of the class 
    def __init__(self , first_name , secound_name ) -> None:  # constructor 
       self.first_name = first_name
       self.secound_name = secound_name
    
    def fullName(self): # based on the explaination it's mention they need first instance for access to the internal parametes 
        print(self.first_name)  # not like static lagugage " kalin waliw eketa access wenna oyaya self instance eke parameter ekaka widihata send karanna one "
        return f"{self.first_name} {self.secound_name}"
        
    
    



    

emp_1 = Employee("shavendra","Ekanayake")
emp_2 = Employee("kanishke" ,"Ekanayake") 

print(emp_1.first_name)
print(emp_2.first_name)


print(emp_1.fullName())







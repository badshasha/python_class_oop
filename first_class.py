# code by 'badshasha'
# purpose : learning python oop concept 


# learning class variables : static information 

from tkinter import E
from xmlrpc.client import boolean


class Employee: 

    # create static varible 
    raise_amount = 1.04
    number_of_emp = 0


    def __init__(self , first_name , secound_name , pay ) -> None:  
       self.first_name = first_name
       self.secound_name = secound_name
       self.pay = pay
       Employee.number_of_emp += 1                 
    
    def fullName(self):                
        return f"{self.first_name} {self.secound_name}"  
    
    def appl_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod 
    def static_raise_amout(cls , amout):  
        cls.raise_amount = 2                


    @classmethod 
    def from_string(cls, emp_stirng):
        name , secound_name , pay = emp_stirng.split('-')
        return cls(name,secound_name,pay)


    @staticmethod
    def is_working(day) -> boolean :
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    def __str__(self):  # spcial method some say magic method 
        return "str working"


    @property
    def email(self)-> str:
        return f"{self.first_name}{self.secound_name}@email.com"
    
    @fullName.setter
    def fullname(self,name):
        self.first_name , self.secound_name = name.split(' ')
    
    @fullName.deleter
    def fullname(self,name):
        pass 





class AnotherInheritance(Employee):
    pass
   
class Deveopers(Employee):          # inheritance 
    def __init__(self, first_name, secound_name, pay,progamming) -> None:  # take all the parameters need for the parenet 
        super().__init__(first_name, secound_name, pay)         # call parent class constructor 
      #  Employee.__init__(self,first_name,secound_name,pay)     # this thing also work but dont use it 
        self.language = progamming
    
    
        




# learning inheritance 

# create instance 
emp1 = AnotherInheritance("shavendra","Ekanayake",1000)
# print(help(emp1))

print(isinstance(emp1,AnotherInheritance))
print(isinstance(emp1,Employee))
print(isinstance(emp1,Deveopers))  # check instance 


# check class 
print(issubclass(Deveopers , Employee))
print(issubclass(AnotherInheritance , Employee))

print(emp1.email)
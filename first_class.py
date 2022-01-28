# code by 'badshasha'
# purpose : learning python oop concept 


# learning class variables : static information 

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

    # problem when we craeting instance method we have to pass instance 
    # so how do we send class to the method 
    # use @classmelthod 

    @classmethod 
    def static_raise_amout(cls , amout):  # cls stand for class 
        cls.raise_amount = 2                # access element using cls 


    @classmethod 
    def from_string(cls, emp_stirng):
        name , secound_name , pay = emp_stirng.split('-')
        return cls(name,secound_name,pay)

    @staticmethod
    def simpleStatic():
        print("working")


    # staticmethod and classmethod are same but class method send class as instance 
    # staticmoethd dont pass any thing 
    # it's behave exacltly tipical function 


    @staticmethod
    def is_working(day) -> boolean :
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    
    # think like this 
        # if you using class instance then user @classmethod 
        # if it's not use @staticmethod 


# create instance 
emp1 = Employee("shavendra","Ekanayake",1000)

# code by 'badshasha'
# purpose : learning python oop concept 


class Employee:  # this thing is a blue print of the class 
   def __init__(self) -> None:  # constructor 
       self.first_name = "Ekanayake"

emp_1 = Employee() # this are the instances of the project 
emp_2 = Employee() # this is a another instance 


print(emp_1)
print(emp_2)


emp_1.first_name = "shavendra"
emp_2.first_name = "pasidu"

print(emp_1.first_name)  # this is not good man 

                    # <__main__.Employee object at 0x7f9d08adbcf8>
                    # <__main__.Employee object at 0x7f9d08adbef0>   each instance have got seperate memeory location 



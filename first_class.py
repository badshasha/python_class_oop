# code by 'badshasha'
# purpose : learning python oop concept 


class Employee:  # this thing is a blue print of the class 
   def __init__(self , first_name , secound_name ) -> None:  # constructor 
       self.first_name = first_name
       self.secound_name = secound_name

emp_1 = Employee("shavendra","Ekanayake")
emp_2 = Employee("kanishke" ,"Ekanayake") 

print(emp_1.first_name)
print(emp_2.first_name)

emp_2.age = 27  # this is why python is not good oop language 






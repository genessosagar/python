# Python Object Oriented Programming
# Method is a function associated with a class
# Class is a blue print for creating instances
# Instance of a class - 

class Employee:
    num_of_emp = 0
    raise_amount =  1.04
    def __init__(self, first, last, pay):       # This __init__ is initialise or constructor
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@abc.com'
        self.pay = pay

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)    # This is good and recommended

# emp_1 and emp_2 are the instance of class Employee
emp_1 = Employee('Sagar', 'Gadda', 5000)
emp_2 = Employee('Niharika', 'Nichenametla', 6000)

# Instance variable contains data that is unique to each instance, we can manually create them

# print(emp_1)
# print(emp_2)

# Manually defining the instance variables - This is not a recommended approach, so I will comment them

# emp_1.first = 'Sagar'
# emp_1.last = 'Gadda'
# emp_1.email = 'Sagar.Gadda@abc.com'
# emp_1.pay = 5000

# emp_2.first = 'Niharika'
# emp_2.last = 'Nichenametla'
# emp_2.email = 'Niharika.Nichenametla@abc.com'
# emp_2.pay = 6000

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# We can access class variables from both class itself and instance as well
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print(Employee.__dict__)
# print(emp_1.__dict__)

Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('*'*50)
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('*'*50)
print(Employee.num_of_emp)
# Regular methods will automatically take instance as the first argument
# Class methods will automatically take class as the first argument
# Static methods will not take instance or class as the first argument

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
    
    @classmethod    # For class methods the first argument will be class not the instance as in regular method
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Sagar', 'Gadda', 5000)
emp_2 = Employee('Niharika', 'Nichenametla', 6000)

print('Before using the class method')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Use class method and change the raise amount
print('After using the class method')
Employee.set_raise_amt(1.05)
# We can even run the class method using the instance as well, but there is no use or doesn't make much sense to do in this way
emp_1.set_raise_amt(1.06)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Parsing a string and getting the first, last and pay
# The following commented lines can be achieved using the class method - from_string defined in the class
# emp_str_1 = 'Neera-Gadda-7000'
# emp_str_2 = 'Sitara-Gadda-4500'
# emp_str_3 = 'Honey-Gadda-9000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.email)
# print(new_emp_1.pay)


emp_str_1 = 'Neera-Gadda-7000'
emp_str_2 = 'Sitara-Gadda-4500'
emp_str_3 = 'Honey-Gadda-9000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))


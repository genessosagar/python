# repr - unambiguous representation of object and used for debugging and logging
# str - is more of a readable representation of an object - used to display to an end user

class Employee:

    raise_amount =  1.04

    def __init__(self, first, last, pay):       # This __init__ is initialise or constructor
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@abc.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)    # This is good and recommended
    
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Sagar', 'Gadda', 5000)
emp_2 = Employee('Niharika', 'Nichenametla', 6000)

print(emp_1) # Print this before writing __repr__ method and after creating repr method
# Output of the above command looks something like this - <__main__.Employee object at 0x7fab1e43afd0>
# The unambiguous output can be made clear by creating a __repr__ method

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(1 + 2)
print(int.__add__(1, 2))

print('a' + 'b')
print(str.__add__('a', 'b'))

print(emp_1 + emp_2)

print(len('Test'))
print('Test'.__len__())

print(len(emp_1))
print(len(emp_2))
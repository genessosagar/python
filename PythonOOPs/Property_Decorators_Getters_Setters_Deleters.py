# Property Decorator - We will define a method in a class and we will be able to access it as an attribute

class Employee:
    
    def __init__(self, first, last, pay):       # This __init__ is initialise or constructor
        self.first = first
        self.last = last
        #self.email = self.first + '.' + self.last + '@abc.com'
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@abc.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None
    
emp_1 = Employee('Sagar', 'Gadda', 9000)
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first = 'David'
print('After assigning new first name')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'Niharika Nichenametla'
print('After assigning setter')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
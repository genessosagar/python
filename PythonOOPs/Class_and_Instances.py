# # Python Object Oriented Programming
# # Method is a function associated with a class
# # Class is a blue print for creating instances
# # Instance of a class - 

# class Employee:
#     num_of_emp = 0
#     raise_amount =  1.04
#     def __init__(self, first, last, pay):       # This __init__ is initialise or constructor
#         self.first = first
#         self.last = last
#         self.email = self.first + '.' + self.last + '@abc.com'
#         self.pay = pay

#         Employee.num_of_emp += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     def apply_raise(self):
#         # self.pay = int(self.pay * Employee.raise_amount)
#         self.pay = int(self.pay * self.raise_amount)    # This is good and recommended

# # emp_1 and emp_2 are the instance of class Employee
# emp_1 = Employee('Sagar', 'Gadda', 5000)
# emp_2 = Employee('Niharika', 'Nichenametla', 6000)

# # Instance variable contains data that is unique to each instance, we can manually create them

# # print(emp_1)
# # print(emp_2)

# # Manually defining the instance variables - This is not a recommended approach, so I will comment them

# # emp_1.first = 'Sagar'
# # emp_1.last = 'Gadda'
# # emp_1.email = 'Sagar.Gadda@abc.com'
# # emp_1.pay = 5000

# # emp_2.first = 'Niharika'
# # emp_2.last = 'Nichenametla'
# # emp_2.email = 'Niharika.Nichenametla@abc.com'
# # emp_2.pay = 6000

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())
# print(Employee.fullname(emp_1))
# print(Employee.fullname(emp_2))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# # We can access class variables from both class itself and instance as well
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# # print(Employee.__dict__)
# # print(emp_1.__dict__)

# Employee.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print('*'*50)
# emp_1.raise_amount = 1.06
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print('*'*50)
# print(Employee.num_of_emp)

# niharika

# class Employee:
#     pass
# emp1 = Employee()
# emp2 = Employee()

# print(emp1)
# print(emp2)

# emp1.first = "niharika"

# print(emp1.first)


# class employee2:
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
# emp1 = employee2('niha', 'honey')
# emp2 = employee2('neera', 'sitara')      
# print(emp1)
# print(emp2)  

# class employee3:

#     def __init__(self,first,last):
#         self.fname = first
#         self.lname = last
#     def fullname(self):
#         print(f'{self.fname} {self.lname}')


# emp1 = employee3('sagar', 'gadda')
# emp2 = employee3('neera', 'sitara')
# print(emp1.fname)
# emp1.fullname()

# employee3.fullname(emp2)

# class emp:
#     hike = 50
#     num_emp = 0
#     def __init__(self,name,pay):
#         self.name = name
#         self.pay = pay
#         emp.num_emp = emp.num_emp + 1
#     def new_pay(self):
#         self.pay = self.pay + (self.hike * self.pay) / 100
#         print(self.pay)

# e1 = emp('vinnie',100)
# e2 = emp('disney',200)

# emp.new_pay(e2)
# e1.hike = 90
# e1.new_pay()
# print(emp.num_emp)

# Niharika
class emp:
    raise_amt = 1.05
    def __init__(self,name,pay):
        self.name = name
        self.pay  = pay

    def new_pay(self):
        self.pay = self.pay * self.raise_amt    

emp1 = emp('niha', 100)


class dev(emp):
    # pass
    raise_amt = 1.1
    def __init__(self,name,pay,id):
        # super().__init__(name,pay)
        emp.__init__(self,name,pay)
        self.id = id
    
dev1 = dev('honey', 1000,1)

class manager(emp):
    def __init__(self,name,pay,staff=None):
        super().__init__(name,pay)
        if staff is None:
            self.staff = []
        else:
            self.staff = staff    
    def add_emp(self,person):
        if person not in self.staff:
            self.staff.append(person) 
    def rem_emp(self,person):
        if person in self.staff:
            self.staff.remove(person)
    def list_emp(self):
        if self.staff == []:
            print(self.name , 'No staff')
        else:    
            for person in self.staff:
                print(self.name, person.name)
man1 = manager('HR',900,[dev1])

man2 = manager('Admin',500,[emp1])

# print(help(person))
# man1.list_emp()
# man1.add_emp(emp1)
man2.rem_emp(emp1)
man1.list_emp()
man2.list_emp()

# print(man1.name,man1.staff)
# print(man2.name,man2.staff)
# print(dev1.name)
# print(dev1.id)
# print(dev1.pay)
# dev1.new_pay()
# print(dev1.pay)
# print(emp1.pay)
# emp1.new_pay()
# print(emp1.pay)
# # print(help(dev))


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

class Developer(Employee):          # Inherited Employee class
    raise_amount = 1.06
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Neera', 'Gadda', 5000, 'Python')
dev_2 = Developer('Sitara', 'Gadda', 4000, 'Go')


#print(help(Developer))
# First the Developer class will search for __init__ method in the Developer class, it will inherit Employee class if not found in developer class

print(dev_1.email)
print(dev_2.email)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)
print(dev_1.prog_lang)
print(dev_2.prog_lang)


mgr_1 = Manager('Sagar', 'Gadda', 8000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
print(mgr_1.email)
mgr_1.print_emps()

# isinstance
# issubclass

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))
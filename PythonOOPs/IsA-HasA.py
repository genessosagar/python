class car:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    def getcarinfo(self):
        print('car:{},colour:{}'.format(self.name,self.colour))

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eathabits(self):
        print('Eat sweets')

class Employee(person):
    def __init__(self,name,age,id,sal,car):
        super().__init__(name,age)
        self.id = id
        self.sal = sal
        self.car = car
    def work(self):
        print('cooking')
    def empinfo(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.sal)
        self.car.getcarinfo()

car = car('Honda', 'Red')
emp = Employee('Niha',32,3,1000,car)
emp.empinfo()
emp.work()

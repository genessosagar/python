# class Engine:
#     colour = 'black'
#     def test1(self):
        
#         print("Inside test1 of Engine()")
# class car:
#     def __init__(self):
#         self.engine = Engine()
#     def car1(self):
#         print('inside car1 of car')

# c = car()
# c.engine.test1()
# c.car1()
# print(c.engine.colour)



# Code reusability.
# 2nd example 

class car:
    def __init__(self,name,colour):
        self.name = name 
        self.colour = colour
    def carinfo(self):
        print('car:{}, colour:{}'.format(self.name,self.colour))
        # print('here')

# print(c.name, c.colour)
# c.carinfo()

class employee:
    def __init__(self,name,age,car):
        self.name = name
        self.age = age
        self.car = car
    def getemp(self):
        b = self.car.carinfo()
        print(self.name, self.age)
        self.car.carinfo()
car = car('honda','black')        
e = employee('niharika', 32, car)
e.getemp()
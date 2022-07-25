# Functions

def hello_func():
    pass

print(hello_func)       # This will not execute the function
print(hello_func())     # Executes the function

def hello_world():
    print('Hello World.')

hello_world()

# DRY - Do not repeat yourself
print('Hello World!')
print('Hello World!')
print('Hello World!')
print('Hello World!')

hello_world()
hello_world()
hello_world()
hello_world()

def hello_return():
    return 'Hello Return!'

hello_return()      # This will not print anything
print(hello_return())
print(hello_return().upper())

print('-'*50)
print('Passing parameters to function')
print('-'*50)

def hello_greet(greeting, country = 'India'):
    return f'{greeting}, Sagar! Welcome to {country}'

print(hello_greet('Good Morning', country = 'America'))
print(hello_greet('Good Night', 'Spain'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# args will be in the form of Tuple
# kwargs = Key Word Arguments in the form of a Dictionary

student_info('Maths', 'Physics', 'Chemistry', name = 'Sagar', age = 18, gender = 'Male')

courses = ['Maths', 'Physics', 'Chemistry']
info = {'name': 'Sagar', 'age': 18, 'gender': 'Male'}

print('Args and Kwargs')
student_info(courses, info)
student_info(*courses, **info)
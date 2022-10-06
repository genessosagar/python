sample_list = ['abc', 123, 'def', ['test', 'nest', 456], 'sagar', 890]
tuple_1 = ('Games', 'Telugu', 'English', 'Hindi', 'Maths', 'Physics', 'Social', 'Biology')
set_1 = {'Games', 'Telugu', 'English', 'Hindi', 'Maths', 'Physics', 'Social', 'Biology'}
student_dict = {
    'name': 'Sagar', 
    'age': 18, 
    'courses': ['Maths', 'Physics', 'Chemistry']
}




num = {1,2,3,4,5}

for i in num:
    print(i)

for i,j in student_dict.items():
    print(i,j)


print(student_dict)

# FUNCTIONS:

def function1():
    print('hi'
    )
function1()



def func2(name,age):
    print(f'Hi {name} {age}')


func2('niharika',10)

# def func3(*args, **kwargs):
#     print(args)
#     print(kwargs)

# func3(10,20,'hi', name = 'honey', gender = 'f' )    

def function_args(*args, **kwargs):
    print(args)
    print(kwargs)

function_args('niha',32, name = 'neera', name1 = 'sitara')    


def func4(*args, **kwargs):
    print(args)
    print(kwargs)

a = 1,2,'Uk'
b = {'name': 'sitara', 'sister': 'neera'}


func4(a,b)

func4(*a,**b)

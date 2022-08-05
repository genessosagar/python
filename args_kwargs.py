# *args
# **kwargs - keyword arguments

def my_func(*args, **kwargs):
    print('Hello World', args, kwargs)

my_func("abc", "def", "ghi", 123, 456, 789, name = 'sagar', age = 18, gender = 'Male')

def my_func(arg_1, *args, **kwargs):
    print('Hello World', args, kwargs, arg_1)

my_func("abc", "def", "ghi", 123, 456, 789, name = 'sagar', age = 18, gender = 'Male')
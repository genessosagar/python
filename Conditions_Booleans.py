# Comparisons
# Equal
# Not 
from platform import python_branch


print('True Condition')
if True:
    print("True Condition")

print('False Condition')
if False:
    print("False Condition")

language = 'NodeJS'

if language == 'Python':
    print('Language is {}'.format(language))
elif language == 'Java':
    print('Language is {}'.format(language))
elif language == 'NodeJS':
    print(f'Language is {language}')
else:
    print(f'Language is {language}, not Python')

# Boolean Operations
# and
# or
# not

user = 'Admin'
role = 'DevOps'
if user == 'Admin' and role == 'Manager':
    print('Admin Manager')
else:
    print('Not Admin Manager')

logged_in = True
if not logged_in:
    print('Please Login')
else:
    print('Welcome')


# Object Identity - is
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(id(a))
print(id(b))
print(a is b)


a = [1, 2, 3]
b = a
print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(id(a) == id(b))


if False:
    print('Sagar')
else:
    print('Honey')

# False Values
# condition = False
# condition = None
# condition = 0
# condition = [] # False 
# condition = '' # False
# condition = () # False
condition = {} # False

# condition = 'somestring' # Evaluates to true

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
# sys module in Python

import sys

print(sys.version)      # version of python interpreter

# Input and Output using sys
# stdin - standard input - internally calls input() function
# stdout - whenever print function is called, it is first written to sys.stdout
# stderr - when exception occurs in python it returns to stderr

# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break
#     print(f'Input: {line}')

# print('Exit')

sys.stdout.write('Printing using sys stdout\n')
print('Printing using print function')

def print_to_stderr(*a):
    print(*a, file = sys.stderr)

print_to_stderr("Hello World!")


# Command Line Arguments using sys module
n = len(sys.argv)
print("Total arguments passed: ", n)
print("Name of the Python script is ", sys.argv[0])

# end parameter in python
print("Welcome to ")
print("United Kingdom")

print('Welcome to', end = " ")
print('United Kingdom', end = ' ')

print("Welcome to ", end = '$')
print('United Kingdom', end = '$')

print('\nArguments passed:', end = ' ')
for i in range(1, n):
    print(sys.argv[i], end = ' ')

# Addition
sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])
print(f'\nThe sum of all argument is {sum}')

# Exiting the program
age = 18
if age < 18:
    sys.exit("Age is less than 18")
else:
    print("Age is not less than 18")

print("This will not print based age less than 18 and sys.exit in the if condition, This will print if the age is above or equal to 18")

print(sys.path)     # Python interpreter will search for the required module in this list of paths refer os module for adding custom path
print(sys.modules)  # Returns the name of Python modules that the current shell has imported




# Where do python looks for modules
# It is in the sys module
import sys
# If the modules are in a different directory than the current file directory, then we will be using the folloiwng command to add that directory to sys.path
sys.path.append('/Users/davidvidyasagar/custom_python_modules')

import my_module
# import my_module as mm                        # Instead of typing my_module we will use mm
# from my_module import find_index, test        # Now we can use directly find_index
# from my_module import *



courses = ['Maths', 'Physics', 'Chemistry', 'Social', 'English', 'Telugu']

index = my_module.find_index(courses, 'Telugu')
print(index)
print(sys.path)     # Prints the list of paths where the python modules are stored


# Set the environment variable for setting Python variable
# Edit the file under the users home dir - ~/.bash_profile
# export PYTHONPATH="/Users/davidvidyasagar/custom_python_modules"
# source .bash_profile
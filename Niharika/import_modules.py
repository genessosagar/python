we can write all the functions in one .py file and use them 
in another files.

like my_module.py
in the original program, use as below


import my_module as mm

name1 = print(mm.func1())

print(name1)

or

from my_module import func1

name = print(func1())

There are many inbuilt modules as os, date etc.


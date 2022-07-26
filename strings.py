print("Hello World")
print('Hello World')
print("Hello \nWorld")
print("Hello \\nWorld")
message = 'Hello World'
print(message)
message1 = 'Sagar\'s World'     # Use Backslash not to read the 's single quote as end of the string
message2 = "Sagar's World"      # Use double quotes if we have single quote used in the string
print(message1)
print(message2)

# Multi Line strings - ''' or """
my_message = """This is the multi line string
I am learning Python
These python files will be uploaded to Github for my reference"""
print(my_message)

# Length of a string
print(len(message))

# Indexing of a string
print(message[0])
print(message[10])
print(message.index('H'))   # Prints the first index of the given character
print(message.find('H'))    # Prints the first index of the given character
print('*'*50)
i = 0
j = len(message)
while i < j:
    print(message[i])
    i += 1

print('*'*50)
print(message[0:5])
print(message[:5])
print(message[6:])
print(message[0:12:1])
print(message[0:12:2])

#To print reverse this is an example for Hello World
print(message[-1::-1])
print(message[10::-1])
print(message[-1:-12:-1])

# Note: All datatypes in python are classes
# Functions defined inside a class is called Method

# String Methods
print(message)
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))        # World starts at the index of 6 result is 6
print(message.find('Universe'))     # Universe is not found so it will be -1
print(message)
new_message = message.replace('World', 'Universe')   # Replace Method
print(message)
print(new_message)

greeting = 'Hello'
name = ' Sagar'

greet_message = greeting + name
print(greet_message)
greet_message = greeting + ', ' + name + '. Welcome!'
print(greet_message)

# String Formatting - Place holders
greet_message = '{}, {}. Welcome!'.format(greeting, name)
print(greet_message)

# F string formatting
greet_message = f'{greeting}, {name.upper()}. Welcome!'
print(greet_message)

print(dir(str))        # Shows all the variables or methods access to that name variable
print(help(str.lower))        # More information about the string - help / manual for string
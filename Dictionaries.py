# Dictionaries - Key Value Pairs
from unicodedata import name


student = {'name': 'Sagar', 'age': 18, 'courses': ['Maths', 'Physics', 'Chemistry']}
print(student)
print(student['name'])
print(student['age'])
print(student['courses'])
print(student['courses'][1])
print(student['courses'][2])
print(student['courses'][0])

#print(student['phone'])        # Error This will give an error
print(student.get('phone'))     # This will print none
print(student.get('name'))
print(student.get('phone', 'Not Found'))
print(student.get('name', 'Not Found'))

student['phone'] = '1234-5678'
student['name'] = 'Honey'
print(student)

# Update Method
student.update({'name': 'Sagar', 'phone': '3333-3333'})
print(student)

# delete - del
del student['phone']
print(student)

# pop - can be used to delete the key and it returns the deleted value
age = student.pop('age')
print(student)
print(age)

# Length
print(len(student))

# Keys and values
student['age'] = 18
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
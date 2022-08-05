sample_list = ['abc', 123, 'def', ['test', 'nest', 456], 'sagar', 890]
print(sample_list)
names = ['Sagar', 'Honey', 'Neera', 'Sitara']
courses = ['Telugu', 'English', 'Hindi', 'Maths', 'Physics', 'Social']
languages = ['Python', 'Java', 'NodeJS', 'C', 'Go']
print(names)
print(len(names))
print(names[0])
print(names[1])
print(names[0:4])
print(courses)
print(len(courses))
print(languages)
print(len(languages))
print(languages[-1])
print(languages[-1::-1])

# Append Method to a list will append a value at the end of the list
courses.append('Biology')
print(courses)

courses = courses + ['Civics']
print(courses)

# Insert method will help to insert a new value to the desired position in the list, it takes two arguments
courses.insert(0, 'Games')
print(courses)

# Extend method - Multiple values we want to add to a list
Teachers = ['abc', 'def', 'ghi', 'jkl']
Students = ['MNO', 'PQR', 'STU']
Teachers.insert(0, Students)
print(Teachers)
print(Teachers[0])
print(Teachers[0][1])
print(Teachers[1])
Teachers.extend(Students)
print(Teachers)
Teachers.remove('STU')
print(Teachers)
popped = Teachers.pop()  # By default removes the last value of the list
print(popped)
print(Teachers)

# Reverse the list 
print(names)
names.reverse()
print(names)

# Sort in alphabetical order
names.sort()
print(names)
names.sort(reverse=True)
print(names)

nums = [89, 45, 67, 19, 42, 38, 24]
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# Sorted Function will not sort and store in the same variable we have to store them in the variable
sorted_nums = sorted(nums)
print(sorted_nums)

# Min, Max and Sum
print(min(nums))
print(max(nums))
print(sum(nums))

# Find Index
print(courses)
print(courses.index('Physics'))
# print(courses.index('Art')) # Value error

# Check if the value is in our list or not - use in
print('Arts' in courses)
print('Arts' not in courses)
print('Maths' in courses)

for item in courses:
    print(item)

for i in courses:
    print(i)

# To access the index and value in the list then we use the enumerate function
for index, item in enumerate(courses):  # Here index and item are user defined variables
    print(index, item) 

print("Start the index from 1 instead of 0")
for index, item in enumerate(courses, start=1):
    print(index, item)

# Convert the list of values into a comma separated string or - string
course_str = ', '.join(courses)
print(course_str)
print(type(course_str))
course_str = ' - '.join(courses)
print(course_str)
new_list = course_str.split(' - ')
print(new_list)
print(type(new_list))


# TUPLES - Immutable - Lists are mutable
tuple_1 = ('Games', 'Telugu', 'English', 'Hindi', 'Maths', 'Physics', 'Social', 'Biology')
tuple_2 = tuple_1
print("Tuples as example")
print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Arts'
# Any mehtod which is trying to mutate the value of a tuple, will not work on tuple unlike list


# Sets - Donot really care about the order of the values in the sets
set_1 = {'Games', 'Telugu', 'English', 'Hindi', 'Maths', 'Physics', 'Social', 'Biology'}
set_2 = {'Geography', 'English', 'History', 'Botany', 'Zoology', 'Telugu'}
print(set_1)
# Sets do not support duplicate values
# Sets are optimised for finding if the value is in the provided set or not
print('Games' in set_1)
print(set_1.intersection(set_2))    # Common in both the sets
print(set_1.difference(set_2))      # Difference between the set_1 and set_2, other courses
print(set_1.union(set_2))           # All courses in both sets

# Creating empty lists, tuples and sets
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This will not create empty set, it will create empty dictionary
empty_set = set()
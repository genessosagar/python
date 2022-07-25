import random
import math
import datetime
import calendar
import os
import antigravity      # This module will open up a page in teh web browser

courses = ['Maths', 'Physics', 'Chemistry', 'Social', 'English', 'Telugu']

random_course = random.choice(courses)

print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)      # All the standard libraries are stored here
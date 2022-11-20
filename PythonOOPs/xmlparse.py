

# import os
# curr_dir = os.getcwd()

# print(curr_dir)

# contents = os.listdir(curr_dir)

# print(contents)

# print('file.xml' in contents)


import xml.etree.ElementTree as ET
tree1 = ET.parse('file.xml')
root = tree1.getroot()

for child in root:
    print(child.tag, child.attrib)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)    
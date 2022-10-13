
f = open('test.txt','r')  
print(f.mode)
print(f.name)

f.close()


with open('test.txt','r') as f:
    print(f.name)

when we use with(), it will close the file explicitly when the block is ended.


Using with is called as ******Context Manager ********


f.readline()
f.read()
f.read(100) - reads first 100 characters.

a = f.read(100)

while len(a) > 0:
    print(a, end='*') 

# f.seek(0) - to assign the position 

# This creates a new file and writes 'Firstline' to that file.

with open('test2.txt', 'w') as f:
    f.write('Firstline')    

# To create a copy of file.


with open('test1.py', 'r') as rf:
    with open('test1_copy.py', 'w') as wf:
        for line in rf:
            wf.write(line)

for binary files, use rb and wb

# for csv files import csv module and use csv.reader()


import csv

with open('a.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        print(i)
        print(i[2]) - only third value in a file.

    
with open('a.csv', 'r') as csv_file:
    with open('b.csv', 'w') as copy_file:

    csv_writer = csv.writer(copy_file, delimiter = '-')
    for i in csv_reader:
        csv_writer.writerow(i)
      
# Dictreader and Dictwriter to get values as key value pair





    


# File Objects
# r - read
# w - write
# a - append
# r+ - read and write
# rb - read in binary mode used for image files
# wb - write in binary mode can be used for image files

# Not a recommended approach
f = open('file.txt', 'r')
print(f.name)
print(f.mode)
f.close()   # ALways important to close the file when we open it

# Use context manager Recommended - This block will automatically closes the file
with open('file.txt', 'r') as f:
    # Recommended not to read the lines in the following format
    # As it is reading the entire content of the file at once
    # This will cause memory issues if the file is large
    # f_contents = f.read()
    # f_contentlines = f.readlines()
    # print(f_contents)
    # print(f_contentlines)
    # f_readline = f.readline()
    # print(f_readline, end = '')           # readline will print only the first line use it again it will print another line
    # f_readline = f.readline()
    # print(f_readline, end = '')

    # Instead use for loop
    # for line in f:
    #     print(line, end='')

    # Instead of reading the entire content of a file using read() we can specify the size as a parameter
    f_content = f.read(100)
    print(f_content)
    # Remaining content
    # f.seek(0)       # Instead of continuting from the remaining content, it prints from the first position 0
    f_content = f.read(100)
    print(f_content)

    # size_to_read = 100
    # f_content = f.read(size_to_read)
    # print(f.tell())     # Tell the position
    # while len(f_content) > 0:
    #     print(f_content, end = '')
    #     f_content = f.read(size_to_read)

# Writing to a file
with open('file2.txt', 'w') as f:       # If the file does not exist it will create a new file, if the file exists it will overwrite it, if we don't want to overwrite use a to append
    f.write('Test')
    f.seek(0)   # This will write from the first - position
    f.write('R')    # It will become Rest if we are using the seek

# Copy the content of a file to a new file
with open('file.txt', 'r') as rf:
    with open('file_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


print()
print(f.name)
#print(f.read())     # Error closed file we are opening
print(f.closed)

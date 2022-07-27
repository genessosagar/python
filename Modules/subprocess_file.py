from cgi import test
import subprocess


# subprocess.run('ls')
# subprocess.run('ls -la', shell = True)   # Shell argument is required
# subprocess.run(['ls', '-la'])       # First item is the command and second item is the argument for that command
# p1 = subprocess.run(['ls', '-la'])
# print(p1)
# print(p1.args)
# print(p1.returncode)
# print(p1.stdout)

# To capture the output to a variable then we use capture_output=True - captures output to the variable p1 
# p1 = subprocess.run(['ls', '-la'], capture_output=True)
# print(p1.stdout)
# print(p1.stdout.decode())

# or 
# p1 = subprocess.run(['ls', '-la'], capture_output=True, text = True)
# print(p1.stdout)


# OR
# p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text = True)
# print(p1.stdout)

# Send the output to a file

# with open('output.txt', 'w') as f:
#     p1 = subprocess.run(['ls', '-la'], stdout=f, text = True)

# If there is an error in the command - Listing the file420.txt that does not exist
# p1 = subprocess.run(['ls', '-la', 'file420.txt'], capture_output=True, text=True)
# print(p1.stderr, end='')
# print(p1.returncode)

# If we want the python ton throw an exception then we use check=True
# p2 = subprocess.run(['ls', '-la', 'file420.txt'], capture_output=True, text=True, check=True)

# To ignore the errors we can redirect them to DEVNULL
# p1 = subprocess.run(['ls', '-la', 'file420.txt'], stderr=subprocess.DEVNULL)
# print(p1.stderr)

# Take the output of one command and give it to another command

p1 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True)
print(p1.stdout)

p2 = subprocess.run(['grep', '-n', 'command'], capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)

# We can use the shell to do the same thing
p1 = subprocess.run('cat test.txt | grep -n testing', capture_output=True, text=True, shell=True)
print(p1.stdout)

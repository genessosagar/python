import os
from datetime import datetime

print(dir(os))      # Lists all attributes and method within the os module
print(os.getcwd())  # Get current working dirctory
os.chdir('/Users/davidvidyasagar/') # Change directory
print(os.getcwd())
print(os.listdir())
os.mkdir('os-dir')
# os.makedirs('os-dir/os-sub-dir/multiple-sub-dirs')
# os.rmdir('os-dir')
# os.removedirs('os-dir/os-sub-dir/multiple-sub-dirs')
os.rename('os-dir', 'remote-dir')           # Renames folder or a directory
print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_mtime)         # Last modification time
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# os.walt - Three value syntax tuple
# for dirpath, dirnames, filenames in os.walk('/Users/davidvidyasagar/'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)

# Environment variable
print(os.environ.get('PATH'))
print(os.environ)   # Prints all the environment variables
print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'demo.txt')        # For path
print(file_path)

print(os.path.basename('/tmp/test.txt'))    # Prints file name
print(os.path.dirname('/tmp/test.txt'))     # Prints dirname /tmp
print(os.path.split('/tmp/test.txt'))       # Prints both dirname and file name
print(os.path.exists('/tmp/test.txt'))      # Prints if the file exists
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))    # Path and extension are printed separately
print(dir(os.path))
# Try and Except for Error Handling
# This file has errors - make sure you understand the code

# f = open('sagarfile.txt')   # If the file sagarfile.txt is not availble, it is going to throw an error - FileNotFoundError
# Instead we can place the above command in the try block

try:
    f = open('sagar_file.txt')
except Exception:       # Here the exception is vague - it does not specify which exception - In the above scenario - FileNotFoundError exception
    print("Sorry! this file does not available")

try:
    f = open('sagarfile.txt')
    var = bad_var
except FileNotFoundError:       # It is good to place specific exceptions at the top and general ones in the bottom
    print("Sorry! this file does not available")
except Exception:
    print('Sorry! Something went wrong')


print('If we donot want to print the custom exception and print the actual exception then capture the exception "as" below')
try:
    f = open('sagarfile.txt')
    # var = bad_var
except FileNotFoundError:       # It is good to place specific exceptions at the top and general ones in the bottom
    print("Sorry! this file does not available")
except Exception as e:
    print(e)


print('')
print('Else block - executes if there is no exception')
print('Finally block executes, no matter even if we have an exception')
try:
    f = open('sagarfile.txt')
    # var = bad_var
except FileNotFoundError:       # It is good to place specific exceptions at the top and general ones in the bottom
    print("Sorry! this file does not available")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('This is printing even we have the bad_var exception or without exception')


print('')
print('Manual exceptions')
try:
    f = open('sagarfile.txt')
    if f.name == 'sagarfile.txt':
        raise Exception
except FileNotFoundError:       # It is good to place specific exceptions at the top and general ones in the bottom
    print("Sorry! this file does not available")
except Exception:
    print('Error! Error!! Error!!!')
else:
    print(f.read())
    f.close()
finally:
    print('This is printing even we have the bad_var exception or without exception')

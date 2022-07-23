from ast import Num


num1 = 3
num2 = 3.14
print(type(num1))
print(type(num2))

# Arithmetic Operators
# Addition +
print(3 + 2)
# Subtraction -
print(3 - 2)
# Multiplication *
print(3 * 2)
# Division /
print(3 / 2)
# Floor Division - // - It drops the decimal and shows only the before decimal
print(3 // 2)
# Exponent **
print(3 ** 2)
# Modulus % - we will ge the remainder as the output
print(3 % 2)

print(3 * 2 + 1)
print(3 * (2 + 1))

# Incrementing the number
num = 1
print(num)
num = num + 1
print(num)

num += 1
print(num)

num *= 10
print(num)

# Absolute Value
print("Absolute Value")
print(abs(-3))

# Round the value
print("Rounding to nearest integer")
print(round(3.75))  # This will round the value to nearest integer
print(round(3.75, 1)) # Round to the first digit after the decimal
print(round(3.25))  # Output - 3
print(round(3.50))  # Output - 4

# Comparison Operators - Returns True or False values
print("Comparison Operators")
num_1 = 3
num_2 = 2
# Equal =
print(num_1 == num_2)
print(num_1 != num_2) # Not equal to !=
print(num_1 > num_2) # Greater than >
print(num_1 < num_2) # Less than <
print(num_1 >= num_2) # Greater than or equal to >=
print(num_1 <= num_2) # Less than or equal to <= 

a = '100'
b = '200'
print(a + b)

# Casting
a = int(a)
b = int(b)
print(a + b)

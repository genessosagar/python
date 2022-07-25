# For
# Break
# Continue
# While
# Range

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Foundit!')
        # break
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(10):
    print(i)

print('-'*50)

for i in range(1, 11):
    print(i)


# While Loop
x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

y = 0
while True:
    if y == 5:
        break
    print(y)
    y += 1

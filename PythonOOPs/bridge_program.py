
import random
list = random.sample(range(1, 10), 4)
print(list)
list.sort()
print(list)
cnt = len(list)
print('Total time taken is ' + str((3 * list[1]) + list[cnt-1] + list[0]))



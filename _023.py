#map

oneTo10 = range(1,11)

def dbl_num(num):
    return num * 2

print(list(map(dbl_num, oneTo10)))

print(list(map((lambda x: x * 3), oneTo10)))

aList = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))

print(aList)

#filter
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))

"""
Find the multiples of 9 from a random 100 value list with values
between 1 and 1000
"""
"""
Generate a random list
randint(1,1000)
use range to generate 100 values
Use mod to find multiples of 9
"""
import random
randList = list(random.randint(1, 1001) for i in range(100))
print(list(filter((lambda x: x % 9 == 0), randList)))

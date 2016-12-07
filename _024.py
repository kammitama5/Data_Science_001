#reduce => import from functools

from functools import reduce

print(reduce((lambda x, y: x + y), range(1, 1000)))

#gives sum of all numbers in range


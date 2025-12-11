# higher order function = take function as arguments
# take iterable and return iterable

from functools import reduce


def sqr(x):
    return x**2


l = [1, 2, 3, 4, 5]
print(list(map(sqr, l)))

new_l = list(filter(lambda x: x > 2, l))
print(new_l)

add = reduce(lambda x, y: x + y, l)
print(add)
# [1,2,3,4,5]
# [3,3,4,5]
# [6,4,5]
# [10,5]
# [15]

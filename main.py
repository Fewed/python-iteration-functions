from pif import *

test_list = [0, 1, 2, 3, 4, 5]
test_tuple = (0, 1, 2, 3, 4, 5)
test_list2 = [1, 2, 1, 2, 2, 3, 4, 4, 3, 4, 5]

res = [
    map(lambda x: x ** 2, test_list),
    map(lambda x: x ** 2, test_tuple),
    filter(lambda x: x % 2, test_list),
    filter(lambda x: x % 2, test_tuple),
    reduce(lambda acc, cur: acc + cur, test_list, 0),
    reduce(lambda acc, cur: acc + cur, test_tuple, 0),
    filter(lambda item, i, arr: arr.index(item) == i, test_list2)
]

map(lambda d: print(d), res)

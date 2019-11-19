# tuple
from typing import List, Union, Tuple

tuple1 = (1, 2, 3, 4)
print("tuple1 {} type {}".format(tuple1, type(tuple1)))

print("tuple1[1] = {}".format(tuple1[1]))

# alt + enter  >
tuple2 = 5, 6, 7, 8
print("tuple2 {} type {}".format(tuple2, type(tuple2)))

tuple3 = (9,)
print("tuple3 {} type {}".format(tuple3, type(tuple3)))

tuple4 = 10,
print("tuple4 {} type {}".format(tuple4, type(tuple4)))

t_list = [tuple1, tuple2, tuple3, tuple4]

print(t_list)
print()
for t in t_list[0:len(t_list)]:
    print("{} type {}".format(t, type(t)))
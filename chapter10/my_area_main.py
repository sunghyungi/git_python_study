import chapter10.my_area
from chapter10.my_area import *

print('pi =', chapter10.my_area.PI)
print('square area =', chapter10.my_area.square_area(5))
print('circle area =', chapter10.my_area.circle_area(2))
print(PI, square_area(5))

print(dir(chapter10.my_area))
[print(content) for content in dir(chapter10.my_area)]
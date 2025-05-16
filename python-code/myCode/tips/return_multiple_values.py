def some_function():
    return 1, 'string', 4.5

tuple1 = some_function()

print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point1 = Point(1,2)

print(point1)
print(point1.x)
print(point1.y)

ThreeDPoint = namedtuple('ThreeDPoint', ['x','y','z'])
point2 = ThreeDPoint(7,4,6)
print (point2)
print(point2.x)
print(point2.y)
print(point2.z)

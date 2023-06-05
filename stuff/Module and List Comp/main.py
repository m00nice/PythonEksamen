import math_operations
import list_comp

print("squarify")
print(math_operations.square(3))
print(math_operations.square(4))
print(math_operations.square(5))
print("cubify")
print(math_operations.cube(3))
print(math_operations.cube(4))
print(math_operations.cube(5))

Numbers = list_comp.numbers

squaredNumbers = [math_operations.square(x) for x in Numbers ]
cubeNumbers = [math_operations.cube(x) for x in Numbers ]

print(squaredNumbers)
print(cubeNumbers)
import method
print(method.filter([1, 33, 5, 6, 992], lambda x: x % 3 == 0))
print(method.map([1, 2, 3], lambda x: x * 3))
print(method.reduce([1, 23, 4, 5], lambda x: x * 2))
print(method.find([1, 33, 5, 5, 993], lambda x: x % 3 == 0))
print(method.reject([1, 33, 5, 6, 992], lambda x: x % 3 == 0))
print(method.filter([1,2,3,455,68,91,-2],lambda x: x%3==0))
print(method.filter([1,2,3,455,68,91,-2],lambda x: x>2))
print(method.filter([1,2,3,455,68,91,-2],lambda x: x<0))
print(method.filter([1,2,3,455,68,91,-2],lambda x: x!=1))
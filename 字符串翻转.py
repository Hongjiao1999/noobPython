# 方法1
str1 = "hello world"
print(str1[::-1])


# 方法2
from functools import reduce
str2 = "hello world"
print(reduce(lambda x, y: y + x, str2))


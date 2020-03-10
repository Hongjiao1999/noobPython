str1 = "23456879"
# 方法1
list1 = list(map(int, str1))
print(list1)

# 方法2
list2 = [int(i) for i in str1]
print(list2)

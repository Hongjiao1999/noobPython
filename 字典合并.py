dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# 方法1
combine_dict = {**dict1, **dict2}
print(combine_dict)

# 方法2
dict3 = {}
dict3.update(dict1)
dict3.update(dict2)
print(dict3)

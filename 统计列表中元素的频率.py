# 方法1
from collections import Counter
list1 = ['p', 'P', 'Y', 'y', 't', 't', 'h', 'o', 'o', 'o', 'n']
count = Counter(list1)
print(count)
print(count['P'])
print(count.most_common())

# 方法2
dict1 = {}
for i in list1:
	if i in dict1:
		dict1[i] += 1
	else:
		dict1[i] = 1
print(dict1)
print(max(dict1, key=lambda x: dict1[x]))

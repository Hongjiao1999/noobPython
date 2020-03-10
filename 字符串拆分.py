str1 = "I love python"
str2 = "I/love/python"
str3 = "      I love python         "

print(str1.split())  # 默认按照空格拆分，返回列表类型
print(str2.split('/'))
print(str3.strip())  # 默认去除字符串两边的空格，返回字符串类型
print(type(str3.strip()))

# 去除不想要的字符
str4 = "I /love python."
import re
print(' '.join(re.split('\W+', str4)))
print(type(' '.join(re.split('\W+', str4))))


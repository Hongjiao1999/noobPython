str1 = [1, 2, 3, 4, 5, 6, 7]
str2 = [1, 2, 2, 4, 5, 6, 7]

def if_unique(string):
	if len(string) == len(set(string)):
		print("yes")
	else:
		print("no")

if_unique(str1)
if_unique(str2)


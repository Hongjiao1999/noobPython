str1 = "pkkkp"
str2 = "abcde"

def f(string):
	if string == string[::-1]:
		print("yes")
	else:
		print("no")


f(str1)
f(str2)

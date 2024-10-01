a = int(input("input : "))
b = input()
c = int(input("input : "))

if b == '+':
	print(a + c)
elif b == '-':
	print(a - c)
elif b == '*':
	print(a * c)
elif b == '/':
	if a == 0 or c == 0:
		print("zero division")
	print(a / c)
else:
	print("invalid")

print("clear-----")
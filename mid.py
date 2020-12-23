a=int(input())
b=int(input())
c=int(input())
list = [a, b, c]
min=(min(list))
max=(max(list))
if min == a and max == c:
	print(b)
if min == b and max == a:
	print(c)
if min ==c and max == b:
	print(a) 
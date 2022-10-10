a, b, c, d = int(input()), int(input()), int(input()), int(input())
r = a,c
k = b,d
r = 100 * k 
e = c - a
f = d - b
if (e >= 0) & (f >= 0):
	print(e, f)
else:
	print("No")

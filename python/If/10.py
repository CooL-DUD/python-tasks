m = int(input())
n = int(input())
k = int(input())

ch = (m * n)
if k < ch & ((k % n == 0) or (k % m == 0)):
	print("YES")
else:
	print("NO")
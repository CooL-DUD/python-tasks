n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
s = (a - d) * (a - d) + (b - c) * (b - c) + 1
print(s)
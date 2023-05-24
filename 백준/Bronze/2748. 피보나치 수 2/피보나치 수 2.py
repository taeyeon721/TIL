f0 = 0
f1 = 1
n = int(input())
while n - 2 >= 0:
    f0, f1 = f1, f0+f1
    n -= 1
print(f1)
n = 1
for _ in range(3):
    n *= int(input())
n = list(str(n))
for i in range(10):
    print(n.count(str(i)))

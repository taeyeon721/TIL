b = list(input())
h = 10
for i in range(1, len(b)):
    if b[i-1] == b[i]:
        h += 5
    else:
        h += 10
print(h)
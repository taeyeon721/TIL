x = []
y = []
for _ in range(3):
    A, B = map(int, input().split())
    if A in x:
        x.remove(A)
    else:
        x.append(A)
    if B in y:
        y.remove(B)
    else:
        y.append(B)
print(f'{x[0]} {y[0]}')
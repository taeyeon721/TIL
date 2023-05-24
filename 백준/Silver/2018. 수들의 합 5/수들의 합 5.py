import sys

N = int(sys.stdin.readline())
cnt = 1
s = 1
e = 1
sumV = 1
while e != N:
    if sumV < N:
        e += 1
        sumV += e
    elif sumV == N:
        cnt += 1
        e += 1
        sumV += e
    else:
        sumV -= s
        s += 1
print(cnt)
import sys
input = sys.stdin.readline
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if max(a, b, c) >= a+b+c-max(a, b, c):
        print("Invalid")
    else:
        s = {a, b, c}
        if len(s) == 1:
            print("Equilateral")
        elif len(s) == 2:
            print("Isosceles")
        else:
            print("Scalene")
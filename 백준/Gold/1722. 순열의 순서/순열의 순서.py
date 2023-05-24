import math
import sys

input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
num = list(range(1, N+1))
if lst[0] == 1:
    i = N-1
    k = lst[1]-1
    while i > 0:
        m = math.factorial(i)
        if k // m == 0:
            if k % m == 0:
                break
            else:
                print(num[k//m], end=" ")
                num.pop(k//m)
                i -= 1
        else:
            print(num[k//m], end=" ")
            num.pop(k//m)
            k -= m*(k//m)
            i -= 1
    if num:
        for n in num:
            print(n, end=" ")
else:
    lst = lst[1:]
    ans = 1
    for i in range(1, N):
        for j in range(len(num)):
            if lst[i-1] == num[j]:
                ans += math.factorial(N-i)*j
                num.pop(j)
                break
    print(ans)
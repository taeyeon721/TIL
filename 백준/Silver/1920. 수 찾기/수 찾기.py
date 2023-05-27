import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))
for num in lst:
    if num in A:
        print(1)
    else:
        print(0)
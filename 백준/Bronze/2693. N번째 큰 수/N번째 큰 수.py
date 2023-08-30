import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    print(lst[2])
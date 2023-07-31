import sys
input = sys.stdin.readline


def f(i):
    n = lst[i]
    ans.remove(n)
    if n not in ans:
        f(n)


N = int(input())
lst = [0]
for _ in range(N):
    lst.append(int(input()))
ans = lst[1:]
s = set(range(1, N+1))
s -= set(lst)
for i in s:
    f(i)
print(len(ans))
ans.sort()
for i in ans:
    print(i)
N = int(input())
scoreC, scoreS = 100, 100
for _ in range(N):
    C, S = map(int, input().split())
    if C > S:
        scoreS -= C
    elif C < S:
        scoreC -= S
print(scoreC)
print(scoreS)
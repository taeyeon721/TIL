T = int(input())
for tc in range(T):
    N = int(input())
    maxV = 0
    ans = ''
    for _ in range(N):
        A, B = input().split()
        if maxV < int(B):
            maxV = int(B)
            ans = A
    print(ans)
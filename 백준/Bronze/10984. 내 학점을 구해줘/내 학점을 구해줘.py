T = int(input())
for tc in range(T):
    N = int(input())
    sumC, sumG = 0, 0
    for _ in range(N):
        C, G = map(str, input().split())
        sumC += int(C)
        sumG += float(G) * int(C)
    print(sumC, sumG/sumC)
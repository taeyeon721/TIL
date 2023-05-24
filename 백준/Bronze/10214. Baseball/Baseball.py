T = int(input())
for tc in range(T):
    scoreY, scoreK = 0, 0
    for _ in range(9):
        Y, K = map(int, input().split())
        scoreY += Y
        scoreK += K
    if scoreY > scoreK:
        print('Yonsei')
    elif scoreY < scoreK:
        print('Korea')
    else:
        print('Draw')
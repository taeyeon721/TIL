T = int(input())
for tc in range(T):
    R = input()
    cnt = 0
    s = 0
    for i in range(len(R)):
        if R[i] == 'O':
            cnt += 1
            s += cnt
        else:
            cnt = 0
    print(s)
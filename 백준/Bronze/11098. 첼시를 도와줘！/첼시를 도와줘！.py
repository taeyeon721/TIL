T = int(input())
for tc in range(T):
    C = []
    name = []
    p = int(input())
    for _ in range(p):
        A, B = map(str, input().split())
        C.append(int(A))
        name.append(B)
    print(name[C.index(max(C))])
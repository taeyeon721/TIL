N = int(input())
d = [[0, 0] for _ in range(3)]
for i in range(N):
    lst = list(map(int, input().split()))
    if i == 0:
        d = [[lst[0], lst[0]], [lst[1], lst[1]], [lst[2], lst[2]]]
    else:
        x1 = min(d[0][0]+lst[0], d[1][0]+lst[0])
        x2 = max(d[0][1]+lst[0], d[1][1]+lst[0])
        y1 = min(d[0][0]+lst[1], d[1][0]+lst[1], d[2][0]+lst[1])
        y2 = max(d[0][1] + lst[1], d[1][1] + lst[1], d[2][1] + lst[1])
        z1 = min(d[1][0] + lst[2], d[2][0] + lst[2])
        z2 = max(d[1][1] + lst[2], d[2][1] + lst[2])
        d = [[x1, x2], [y1, y2], [z1, z2]]
print(max(d[0][1], d[1][1], d[2][1]), min(d[0][0], d[1][0], d[2][0]))
T = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(T):
    i = 0
    x, y = 0, 0
    minX, minY, maxX, maxY = 0, 0, 0, 0
    lst = list(input())
    for c in lst:
        if c == 'F':
            x += dx[i]
            y += dy[i]
        elif c == 'B':
            x -= dx[i]
            y -= dy[i]
        elif c == 'L':
            i = (i+1)%4
        elif c == 'R':
            i = (i+4-1)%4
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y
    print((maxX-minX)*(maxY-minY))
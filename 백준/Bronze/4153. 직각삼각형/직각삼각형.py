while True:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break
    else:
        s = 0
        for num in lst:
            s += (num**2)
        if s == 2*(max(lst)**2):
            print('right')
        else:
            print('wrong')
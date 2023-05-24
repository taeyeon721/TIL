while True:
    n = int(input())
    if n == -1:
        break
    i = 1
    x = []
    while i <= (n//2):
        if n % i == 0:
            x.append(i)
        i += 1
    if sum(x) == n:
        for i in range(len(x)):
            x[i] = str(x[i])
        s = ' + '.join(x)
        print(f'{n} = {s}')
    else:
        print(f'{n} is NOT perfect.')
def solution(n):
    answer = hanoi(n, 1, 3, 2)
    
    return answer


def hanoi(n, s, e, a):
    if n == 1:
        res = []
        res.append([s, e])
        return res
    else:
        res = hanoi(n-1, s, a, e)
        res.append([s, e])
        res += hanoi(n-1, a, e, s)
        return res
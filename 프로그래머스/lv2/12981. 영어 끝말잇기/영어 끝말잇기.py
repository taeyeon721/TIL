def solution(n, words):
    word = []
    cnt = 0
    e = words[0][0]
    a, b = 0, 0
    for s in words:
        if s[0] != e:
            break
        if s in word:
            break
        else:
            cnt += 1
            word.append(s)
            e = s[-1]
    if cnt == len(words):
        answer = [0, 0]
    else:
        if (cnt + 1) % n == 0:
            a = n
            b = (cnt + 1) // n
        else:
            a = (cnt + 1) % n
            b = (cnt + 1) // n + 1
        
    answer = [a, b]
    return answer
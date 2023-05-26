while True:
    ans = 'yes'
    s = input()
    if s == '0':
        break
    else:
        for i in range((len(s)//2)+1):
            if s[i] != s[len(s)-i-1]:
                ans = 'no'
    print(ans)
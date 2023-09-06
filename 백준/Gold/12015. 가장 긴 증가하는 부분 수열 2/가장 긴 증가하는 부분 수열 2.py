import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
lst = [0]
for num in A:
    if lst[-1] < num:
        lst.append(num)
    else:
        s = 0
        e = len(lst)
        while s < e:
            mid = (s+e)//2
            if lst[mid] < num:
                s = mid+1
            else:
                e = mid
        lst[e] = num
print(len(lst)-1)
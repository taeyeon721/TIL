N = int(input())
nums = list(map(int, input().split()))
lst = [1]*1001
lst[0], lst[1] = 0, 0

for i in range(2, int(100*(1/2))+1):
    if lst[i] == 1:
        j = 2
        while i*j <= 1000:
            lst[i*j] = 0
            j += 1
cnt = 0
for num in nums:
    if lst[num] == 1:
        cnt += 1
print(cnt)
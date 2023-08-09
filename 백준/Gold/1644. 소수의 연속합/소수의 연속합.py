import math

N = int(input())

# 에라토스테네스의 채
arr = [True]*(N+1)
arr[0] = False
arr[1] = False

for num in range(2, int(math.sqrt(N))+1):
    if arr[num]:
        for mul in range(num*2, N+1, num):
            arr[mul] = False

arr = [i for i in range(2, N+1) if arr[i]] + [0]


# 투 포인터(두 포인터 모두 왼쪽에서 시작)
i = 0
j = 0
subtotal = arr[i]
count = 0

while j < len(arr)-1:
    if subtotal == N:
        count += 1
        subtotal -= arr[i]
        i += 1
        j += 1
        subtotal += arr[j]
    elif subtotal < N:
        j += 1
        subtotal += arr[j]
    else:
        subtotal -= arr[i]
        i += 1
        
print(count)
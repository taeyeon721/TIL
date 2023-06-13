"""
투 포인터
왼쪽과 오른쪽의 블록을 비교하며 물이 채워질 수 있는 양을 계산
왼쪽과 오른쪽 중에서 더 낮은 블록을 기준으로 그 것보다 높은 블록을 만날 때까지
물의 양을 더해줌
"""
H, W = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
left, right = 0, W-1
left_max, right_max = lst[left], lst[right]

while left < right:
    if lst[left] < lst[right]:
        if lst[left]> left_max:
            left_max = lst[left]
        else:
            ans += left_max - lst[left]
        left += 1
    else:
        if lst[right] > right_max:
            right_max = lst[right]
        else:
            ans += right_max - lst[right]
        right -= 1
print(ans)
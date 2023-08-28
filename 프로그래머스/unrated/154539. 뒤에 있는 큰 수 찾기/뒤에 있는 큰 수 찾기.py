def solution(numbers):
    answer = [-1]*len(numbers)
    stack = [0]
    for i in range(1, len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            n = stack.pop()
            answer[n] = numbers[i]
        stack.append(i)
    return answer
def solution(num1, num2):
    answer = 0

    if num1 and num2 > 0 and num1 and num2 <= 100:
        answer = num1 // num2
    return answer

print(solution(10, 5))
print(solution(7,2))
def solution(num1, num2):
    if num1 == num2:
        answer = 1
        return answer
    else:
        answer = -1
        return answer
    if num1 and num2 <= 0 and num1 and num2 >= 10000:
        answer = 0
        return answer
print(solution(2, 3))
print(solution(11, 11))
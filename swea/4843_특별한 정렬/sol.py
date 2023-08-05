import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

# T = int(input())



# for tc in range(1, T+1):
    
#     N = int(input())

    
#     a = list(map(int, input().split()))

#     result = []
    
#     for i in a:

#         left_num = 100
#         right_num = 0

#         while True:

#             if left_num >= i:
#                 left_num = i
#                 result.append(left_num)

#             if right_num <= i:
#                 right_num = i
#                 result.append(left_num)
#         else:
#             break

#         print(result)


# 강사 입력
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = []

    while len(numbers):
        max_num = 0
        for m in range(len(numbers)):
            if max_num < numbers[m]:
                max_num = numbers[m]

        result.append(max_num)
        numbers.remove(max_num)

        min_num = 1000000
        for n in range(len(numbers)):
            if min_num > numbers[n]:
                min_num = numbers[n]

        result.append(min_num)
        numbers.remove(min_num)
        

        if len(result) == 10:
            break

    print(result)
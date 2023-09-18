import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


# T = int(input())

# for tc in range(1, T+1):

#     N = int(input())  
#     numbers = list(map(int, input().split()))

#     # print(N, numbers)
#     # 정렬 후 큰수 작은수 뽑아서 연산
#     # numbers.sort()
#     # result = numbers[-1] - numbers[0]

#     # 첫 번째 number는 비교할 대상이 없으므로 비교값을 세팅해준거임
#     # min_number = 10000000
#     min_number = numbers[0]
#     # max_number = 0
#     max_number = numbers[0]

#     for number in numbers:
#         if min_number > number:
#             min_number = number
        
#         if max_number < number:
#             max_number = number

#     result = max_number - min_number


#     print(f'#{tc} {result}')


# T = int(input())


# for tc in range(1, T+1):

#     N = int(input())

#     a = list(map(int, input().split()))
    
#     t_max = max(a)
#     t_min = min(a)

#     print(t_max-t_min)

# # result = []
# # for _ in range(0, N-1):
# #     print(_)
#     # for t_max in a:
#     #     print(t_max)
#     # if result < t_max:
#     #     result.append(t_max)

# # print(result)


T = int(input())
for i in range(1, T+1):
    N = int(input())

    ai = list(map(int, input().split()))

    # ai.sort()
    # for idx, num in enumerate(ai):

    minnum = min(ai)
    maxnum = max(ai)

    print(maxnum-minnum)

        
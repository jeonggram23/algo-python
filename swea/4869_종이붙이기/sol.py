import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

result = []
sq1 = ''
sq2 = ''
sq3 = ''

# 2/1 사각형

for row1 in range(2):
    for col1 in range(1):
        sq1 = sq1[row1][col1]

# 1/2 사각형

for row2 in range(2):
    for col2 in range(1):
        sq2 = sq2[row2][col2]

# 2/2 사각형

for row3 in range(2):
    for col3 in range(2):
        sq3 = sq3[row3][col3]
        print(sq3)

# for tc in range(1, T+1):
#     sq = int(input())
#     for row in range(20//10):
#         for col in range(sq//10):
#             # print(row,col)
            
            #색칠 시작
            








# 강사 입력

# T = int(input())

# memo = [0, 1, 3]

# for tc in range(1, T+1):
#     N = int(input()) // 10

#memo 배열에 출력시킬 값이 없으면 추가
#     while N >= len(memo):
# #         # n-2 배열에 가로로 작은 사각형 두개를 쌓거나 큰 사각형을 쌓는 방법 (x2)
# #         # n-1 배열에 세로로 작은 사각형 쌓는 방법 하나.
# #         temp = 2 * memo[len(memo)-2] + memo[len(memo)-1]
# #         memo.append(temp)

#     print(memo[N])
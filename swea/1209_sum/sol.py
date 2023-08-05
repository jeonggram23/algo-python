# import sys
# sys.stdin = open('input.txt')

# T = int(input())
# matrix = []
# max = []
# row = 10
# col = 10

# for tc in range(1, T+1):
    
#     numbers = list(map(int, input().split()))
#     matrix.append(numbers)

#     for row in range(101):
#         numberss = list(map(int, input().split()))
#         print(numberss)
    


# 강사 입력
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc =int(input())

    matrix= []

    # 원래는 i, j ,a 등 반복문을 돌리는 요소를 임시로 저장하는 변수
    # _ => 변수를 활용하지 않을 예쩡이라서 변수 이름일 비워 놓겠다는 의미.
    for _ in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)

    

    total = 0

    #가로줄 반복
    for row in range(len(matrix)):
        temp = 0
        for col in range(len(matrix[0])):
            temp += matrix[row][col]
        if total < temp:
            total = temp

    #세로줄 반복
    for col in range(100):
        temp = 0
        for row in range(100):
            temp += matrix[row][col]

        if total < temp:
            total = temp

    # 좌 상단 => 우하단 반복
    for i in range(100):
        temp = 0
        temp += matrix[i][i]
    
    if total < temp:
        total = temp

    # 우상단 => 좌하단 반복
    temp = 0
    for i in range(100):
        temp += matrix[i][99-i]

    if total < temp:
        total = temp

    print(f'#{tc} {total}')
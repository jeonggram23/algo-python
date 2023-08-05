# import sys
# sys.stdin = open('input.txt')
# # N - 건물의 개수
# N = int(input())
# for tc in range(0, N+1):

#     # Nh - 건물의 높이
#     Nh = list(map(int, input().split()))
#     print(Nh)
#     for i, nh in enumerate(Nh):
#         #if i의 nh가 i +- 1과 i +- 2의 건물들보다 큰 지
#         if nh[i] 
    
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    # N - 건물 인덱스
    N = int(input())
    # Nh - 건물의 높이
    Nh = list(map(int, input().split()))

    # print(N, Nh)
    total = 0
    for i in range(N):
        # print(i, Nh[i])
        now = Nh[i]
        


        # 현재 위치의 건물 높이가 0이라면 다음 건물로 이동
        if now == 0:
            continue

        # 나의 위치에 건물이 있는 경우
        else:
            # 양 옆 * 2 건물들의 높이를 비교
            dx = [-2, -1, 1, 2]


            max_tall = 0


            for j in range(4):
                # i : 현재위치
                #dx[j] : 기준 건물을 중심으로 좌우 인덱스
                comp = Nh[i+dx[j]]

                if max_tall < comp:
                    max_tall = comp

            #나머지 네개의 건물보다 내가 더 크다면 조망권 확보
            if now > max_tall:
                view = now - max_tall
                total += view

    print(f'#{tc} {total}')

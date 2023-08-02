def solution(angle):
    answer = 0

    if angle == 180:
        answer = 4
    elif angle < 180:
        answer = 3
    elif angle == 90:
        answer = 2
    elif angle < 90:
        answer = 1
    elif angle <= 0: 
        answer = 0
    else:
        answer = 0
    
    return answer
#오답 1
#결과 ['A', 'A', 'A', 'b', 'b', 'b', 'C', 'C', 'C', 'd', 'd', 'd']
# def solution(strArr):
# 	    answer = []
# 	    for i in range(0, len(strArr)):
# 	        if i % 2 == 0:
# 	            answer += strArr[i].upper()
# 	            # return answer
# 	        else:
# 	            answer += strArr[i].lower()
	            
# 	    return answer
# print(solution(["AAA","BBB","CCC","DDD"]))
    
#과정

# print(solution(["AAA","BBB","CCC","DDD"]))
# a = ["AAA","BBB","CCC","DDD"]
# b = str(a[0])
# b.lower()
# print(b)

# a = ['AbC', 'dEf', 'GuI']
# print(a[0].lower() + a[2].lower())
# b = []
# b.append(a)
# print(b)

#정답
def solution(strArr):
    answer = []
    for i in range(0, len(strArr)):
        if i % 2 != 0:
            answer.append(strArr[i].upper())
            
            # return answer
        else:
            answer.append(strArr[i].lower())
            
    return answer
        
        
solution(["AAA","BBB","CCC","DDD"])
print(solution(["AAA","BBB","CCC","DDD"]))


#enumerate 버전
def solution(strArr):
    res = []
    for i,e in enumerate(strArr):
        if i%2==0:
            res.append(e.lower())
        else:
            res.append(e.upper())
    return res

solution(["AAA","BBB","CCC","DDD"])
print(solution(["AAA","BBB","CCC","DDD"]))
    
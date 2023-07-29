bloodtype = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

# result = {'사과':3}
# a = result['사과']+1
# print(a)

result = {'A': 0, 'O': 0, 'B': 0, 'AB': 0,}

for i in bloodtype:
    if i == 'A':
        pass
    elif i == 'B':
        pass
    elif i == 'O':
        pass
    else:
        pass
print(result)



## 강사 입력
blood_dict ={
    'A': 0,
    'B': 0,
    'AB': 0,
    'O': 0,
}

for blood in bloodtype:
    blood_dict[blood] += 1

print(blood_dict)

# 미리 값을 입력할 수 없을 때
location_list = ['서울', '부산', '서울', '서울', '대전', '제주', '광주', '부산']
#location_list = input()
location_dict = {}

for location in location_list:
    #이미 기록된 도시
    if location in location_dict.keys():
        location_dict[location] += 1
    #처음 등장한 도시
    else:
        location_dict[location] = 1

print(location_dict)
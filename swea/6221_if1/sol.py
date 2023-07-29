import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()



# s + s = draw
# s + r = man2 win
# s + p = man1 win

# r + r = draw
# r + p = man2 win

# p + p = draw

if man1 == '가위' and man2 == '바위':
    print('Result : Man2 Win!')
elif man1 == '가위' and man2 == '보':
    print('Result : Man1 Win!')
elif man1 == '바위' and man2 == '보':
    print('Result : Man2 Win!')
elif man1 == '바위' and man2 == '가위':
    print('Result : Man1 Win!')
elif man1 == '보' and man2 == '가위':
    print('Result : Man2 Win!')
elif man1 == '보' and man2 == '바위':
    print('Result : Man2 Win!')
else:
    print('Result : Draw')


# 강사 입력
# 가위, 바위, 보
# 0       1   2

# 보, (가위)     win2  2
# (바위), 가위   win1  1
# (보), 바위     win1  1
# 가위, (바위)   win2  -1
# 바위, (보)     win2  -1
# (가위), 보     win1  -2

rcp = ['가위', '바위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

#print(man1_idx, man2_idx)

result = man1_idx - man2_idx

#print(result)

if result == 0:
    print('result : draw')
elif result > 0:
    print(f'result : man{result} win.')
else:
    if result == -1:
        print('result : man2 win')
    else:
        print('result : man1 win')
# if man1 == man2:
#     print('Result : Draw')


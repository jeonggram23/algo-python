import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

# T = int(input())

# memo = '(' , ')', '{', '}','[',']'
# count = 0

# for tc in range(1, T+1):
#     print(tc)
#     if '(' in tc:
#         count += 1
#     elif ')' in tc:
#         count -= 1
#     elif '{' in tc:
#         count += 1
#     elif '}' in tc:
#         count -= 1
#     elif '[' in tc:
#         count += 1
#     elif ']' in tc:
#         count -= 1

# 강사 입력

T = int(input())

for tc in range(1, T+1):
    code = input()
    # code = list(input()) 로도 가능
    stack = []

    for char in code:
        if char == '(' or char == '{':
            stack.append(char)
        elif len(stack) and char == ')' and stack[-1] == '(':
            stack.pop()
        elif len(stack) and char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)

    if len(stack) == 0:
        result = 1
    else:
        result = 0

        
        
        
import sys
sys.stdin = open('input.txt')

char = input()

if char.isupper():
    print(f'{char}는 대문자입니다.')
else:
    print(f'{char}는 소문자입니다.')
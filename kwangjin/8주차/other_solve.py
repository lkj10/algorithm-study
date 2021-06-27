import re


def solution(s):
    stack = list()
    for i in s:
        stack.pop() if stack and stack[-1] == i else stack.append(i)
    return 0 if stack else 1

# 정규표현식으로 품. 그러나 시간초과 이슈


def solution(s):
    while re.search('(([a-zA-Z0-9])\\2{1})', s):
        s = re.sub('(([a-zA-Z0-9])\\2{1})', '', s)
    return 0 if s else 1

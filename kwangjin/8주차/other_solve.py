#import re
def solution(s):
    # while re.search('(([a-zA-Z0-9])\\2{1})',s):
    #     s = re.sub('(([a-zA-Z0-9])\\2{1})', '', s)
    # return 0 if s else 1
    stack = list()
    for i in s:
        stack.pop() if stack and stack[-1] == i else stack.append(i)
    return 0 if stack else 1

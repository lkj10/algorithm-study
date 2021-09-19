import sys
from collections import deque
import re
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    cmd = list(input())
    arr_len = int(input())
    List = deque(re.findall(r'\d+', input()))
    dir = 1
    for i in cmd:
        if i == 'R':
            dir *= -1
        if i == 'D':
            if List:
                if dir == 1:
                    List.popleft()
                else : 
                    List.pop()
            else:
                print('error')
                break
    else:
        res = ['[']
        if List:
            if dir == 1 :
                for i in List:
                    res.append(i)
                    res.append(',')
            else:
                for i in reversed(List):
                    res.append(i)
                    res.append(',')
            res.pop()
        res.append(']')
        print(''.join(res))

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
M, N = map(int, input().split())

List = deque([i for i in range(1, M+1)])
result = list()
cnt = 0
while List:
    cnt += 1

    if cnt == N:
        result.append(List.popleft())
        cnt = 0

    else:
        List.append(List.popleft())

print("<", end='')
for i in range(len(result)):
    if i == len(result) - 1:
        print(str(result[i]) + ">")
    else:
        print(result[i], end=', ')
